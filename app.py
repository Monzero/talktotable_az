import streamlit as st
import os
import tempfile
# MODIFIED: Import AzureChatOpenAI instead of ChatOpenAI
from langchain_openai import AzureChatOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.callbacks.streamlit import StreamlitCallbackHandler
from langchain.callbacks.base import BaseCallbackHandler
#import sweetviz as sv

from langchain.schema import AgentAction

import pandas as pd
import io
import tempfile
import json
import re       
        
# Import modularized components
from modules.data_preparation import prepare_dataframe
from modules.agent_tools import create_python_tool
from modules.query_processing import create_guardrail_chain, run_guardrail_loop, extract_query, extract_chat_history_from_string
from modules.dataframe_analyzer import DataFrameAnalyzer, ColumnDescriptionParser, generate_dataset_report_for_llm

# MODIFIED: Add helper function to create Azure OpenAI client with Entra ID
def get_azure_llm(temperature=0, model_name="gpt-35-turbo"):
    """Create Azure OpenAI LLM with Entra ID authentication"""
    endpoint = os.getenv("ENDPOINT_URL", "https://ttt-openai-01.openai.azure.com/")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview")
    
    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://cognitiveservices.azure.com/.default"
    )
    
    return AzureChatOpenAI(
        azure_endpoint=endpoint,
        azure_ad_token_provider=token_provider,
        api_version=api_version,
        azure_deployment=model_name,
        temperature=temperature
    )

            

class StreamlitChatCallbackHandler(BaseCallbackHandler):
    def on_chain_start(self, serialized: dict, inputs: dict, **kwargs) -> None:
        with st.chat_message("assistant"):
            st.markdown("🔄 **Chain started**")
            st.json(inputs)
     
    def on_agent_action(self, action: AgentAction, **kwargs) -> None:
        
        thought = action.log.split("Action")[0].strip()
        
        with st.chat_message("assistant"):
            st.markdown("**🤔 Thought:**")
            st.markdown(action.log)
        
        with st.chat_message("assistant"):
            st.markdown("**Thought:**")
            #st.markdown(action.log)
            st.markdown(f"`{thought}`")

            st.markdown("**Action:**")
            st.markdown(f"`{action.tool}`")

            st.markdown("**Action Input:**")
            st.code(str(action.tool_input), language="python")

    def on_tool_end(self, output: str, **kwargs) -> None:
        with st.chat_message("assistant"):
            st.markdown("**Observation:**")

            # Try to render tabular data if present
            try:
                df = pd.read_fwf(io.StringIO(output))
                if not df.empty and df.shape[1] > 1:
                    st.dataframe(df, use_container_width=True)
                else:
                    st.code(output)
            except Exception:
                st.code(output)            
    
    def on_llm_end(self, response, **kwargs) -> None:
        with st.chat_message("assistant"):
            st.markdown("📝 **LLM Response:**")
            st.markdown(response.generations[0][0].text)


    def on_chain_end(self, outputs: dict, **kwargs) -> None:
        with st.chat_message("assistant"):
            st.markdown("**Chain completed**")
            st.json(outputs)


def get_sample_datasets():
    """
    Get available sample datasets from the sample_data folder.
    Returns dict of {display_name: (csv_path, desc_path)}
    """
    sample_data_folder = "sample_data"
    
    if not os.path.exists(sample_data_folder):
        return {}
    
    datasets = {}
    csv_files = [f for f in os.listdir(sample_data_folder) if f.endswith('.csv')]
    
    for csv_file in csv_files:
        csv_path = os.path.join(sample_data_folder, csv_file)
        
        # Look for corresponding description file
        base_name = csv_file.replace('.csv', '')
        desc_file = f"{base_name}_desc.txt"
        desc_path = os.path.join(sample_data_folder, desc_file)
        
        if not os.path.exists(desc_path):
            desc_path = None
        
        # Use base name as display name
        display_name = base_name.replace('_', ' ').title()
        datasets[display_name] = (csv_path, desc_path)
    
    return datasets


# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # File upload or sample selection
    st.subheader("Data Source")
    
    # Sample dataset selector
    sample_datasets = get_sample_datasets()
    
    use_sample = False
    csv_path = None
    desc_path = None
    
    if sample_datasets:
        st.info(f"Found {len(sample_datasets)} sample dataset(s)")
        selected_sample = st.selectbox(
            "Select a sample dataset",
            ["Upload your own"] + list(sample_datasets.keys())
        )
        
        if selected_sample != "Upload your own":
            use_sample = True
            csv_path, desc_path = sample_datasets[selected_sample]
            st.success(f"Using sample dataset: {selected_sample}")
    
    # File upload section (only show if not using sample)
    if not use_sample:
        uploaded_csv = st.file_uploader("Upload CSV File", type=["csv"])
        uploaded_desc = st.file_uploader(
            "Upload Description File (optional)", 
            type=["txt"],
            help="Upload a text file describing the dataset columns"
        )
        
        if uploaded_csv:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp_csv:
                tmp_csv.write(uploaded_csv.read())
                csv_path = tmp_csv.name
            
            if uploaded_desc:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp_desc:
                    tmp_desc.write(uploaded_desc.read())
                    desc_path = tmp_desc.name
            else:
                desc_path = None
    
    if not sample_datasets and not use_sample:
        st.info("To add sample datasets, create a 'sample_data' folder and add CSV files with optional description files (filename_desc.txt).")
    
    # Model selection (commented out in original)
    # model_name = st.selectbox(
    #     "Select Model",
    #     ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"],
    #     index=0
    # )
    
    # Clear buttons
    st.subheader("Session Management")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        st.session_state.memory_gr = ConversationBufferMemory(memory_key="chat_history", input_key="user_input", return_messages=True)
        st.success("Chat history cleared!")
    
    # if st.button("Start New Session"):
    #     st.session_state.messages = []
    #     st.session_state.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    #     st.session_state.memory_gr = ConversationBufferMemory(memory_key="chat_history", input_key="user_input", return_messages=True)
    #     st.session_state.df = None
    #     st.success("New session started! Please upload a new CSV file.")

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

if "memory_gr" not in st.session_state:
    st.session_state.memory_gr = ConversationBufferMemory(memory_key="chat_history", input_key="user_input", return_messages=True)

if "df" not in st.session_state:
    st.session_state.df = None

if "df_info_str" not in st.session_state:
    st.session_state.df_info_str = ""

if "col_desc_str" not in st.session_state:
    st.session_state.col_desc_str = ""

if "globals_dict" not in st.session_state:
    st.session_state.globals_dict = {}

if "agent" not in st.session_state:
    st.session_state.agent = None

if "guardrail_chain" not in st.session_state:
    st.session_state.guardrail_chain = None

# Main content area
st.title("Talk2Table")

# Load environment variables
load_dotenv()

# MODIFIED: No longer checking for OPENAI_API_KEY, using Azure Entra ID instead
# Check for required Azure environment variables
endpoint = os.getenv("ENDPOINT_URL")
if not endpoint:
    st.error("ENDPOINT_URL not found in .env file. Please add your Azure OpenAI endpoint to continue.")
    st.stop()

# Process files (either uploaded or sample)
if csv_path:
    # MODIFIED: No need to set OPENAI_API_KEY environment variable
    
    # Load dataframe and related information
    df, df_info_str, col_desc_str, globals_dict = prepare_dataframe(csv_path, desc_path)
    
    # MODIFIED: Pass None for API key since we're using Entra ID
    # The generate_dataset_report_for_llm function has been updated to use Azure OpenAI with Entra ID
    # Pass the deployment name as the model_name parameter
    col_desc_str = str(generate_dataset_report_for_llm(
        df, 
        col_desc_str, 
        openai_api_key=None,  # Not used anymore, using Entra ID
        model_name=os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo"),  # Azure deployment name
        verbose=True
    ))
    
    # Generate Sweetviz report (commented out in original)
    #report_file = "sweetviz_report.html"
    #report = sv.analyze(df)
    #report.show_html(report_file)

    # Create a link to open it in new tab
    #st.markdown("### 📊 Open Sweetviz Report")
    #st.markdown(f'<a href="{report_file}" target="_blank">👉 Click here to open report in new tab</a>', unsafe_allow_html=True)
    
    # Store in session state
    st.session_state.df = df
    st.session_state.df_info_str = df_info_str
    st.session_state.col_desc_str = col_desc_str 
    st.session_state.globals_dict = globals_dict
    
    # MODIFIED: Use Azure OpenAI with Entra ID instead of ChatOpenAI
    llm_gr = get_azure_llm(
        temperature=0.4,
        model_name=os.getenv("DEPLOYMENT_NAME", "gpt-4o-mini")
    )
    
    # MODIFIED: Use Azure OpenAI with Entra ID instead of ChatOpenAI
    llm = get_azure_llm(
        temperature=0,
        model_name=os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo")
    )
    
    
    # Create tools for the agent
    tools = create_python_tool(globals_dict, col_desc_str)
    
    # Create guardrail prompt template
    guardrail_prompt = PromptTemplate(
    input_variables=["user_input", "df_info", "col_desc", "chat_history"],
    template="""
    You are a bridge between query tool and user. Your job is to make sense of a user's input and make clear instruction for next tool about what user wants.

    The dataset has the following columns:
    {df_info}
    Based on the columns, you can infer which columns are relevant to the user query.
    
    Please refer to column descriptions for better clarity and how to make sense of the columns:
    {col_desc}

    Conversation so far we have with the user:
    {chat_history}
    You should consider this conversation to add context to the user query. If user hasn't formed full question, look at the last question to understand what could be his full question.
    
    The User query is:
    "{user_input}"

    Instructions:
    1. If the current query refers to something comparative (e.g., "lowest", "most", "that", "then", "it"), use the chat history to determine what the user is referring to.
    2. For example, if user previously asked which team won highest number of matches, and now asking "then what was the score of that team", you should understand that user is asking about the score of the team with highest number of matches.
    3. If the user query is ambiguous or unclear (e.g., refers to something not in columns), ask for clarification.
    4. Once the ask in the query is clear, rephrase it into a precise form for downstream analysis.
    5. If the query is already clear and relevant to the dataset, just rephrase it clearly.
    6. Make sure to not have word 'clarification' in the response if query is clear.
    
    Respond ONLY in one of the following formats:
    - If unclear:
    Clarification Needed: <your clarification question>
    - If clear:
    Rephrased Query: <your improved query>
    """
    )

    # Create guardrail chain
    if st.session_state.guardrail_chain is None:
        st.session_state.guardrail_chain, st.session_state.memory_gr = create_guardrail_chain(llm_gr, guardrail_prompt)
    
    guardrail_chain = st.session_state.guardrail_chain
    memory_gr = st.session_state.memory_gr

    # Create agent if not exists
    if st.session_state.agent is None:
        st.session_state.agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            memory=st.session_state.memory,
            handle_parsing_errors=True,
        )
    
    agent = st.session_state.agent

    # Display DataFrame info
    st.subheader("Dataset Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Size", f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB")
    
    with st.expander("View Dataset Sample"):
        st.dataframe(df.head())
    
    # Display column descriptions if available
    if st.session_state.col_desc_str:
        with st.expander("📋 High level data observation"):
            st.markdown(st.session_state.col_desc_str)

    # Chat interface
    st.subheader("Chat with your Data")

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Ask a question about your dataset"):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Process query
        with st.chat_message("assistant"):
            with st.spinner("Processing your query..."):
                try:
                    # Run guardrail check
                    chat_history_str = extract_chat_history_from_string(str(memory_gr.chat_memory.messages))
                    
                    inputs = {
                        "user_input": prompt,
                        "df_info": st.session_state.df_info_str,
                        "col_desc": st.session_state.col_desc_str,
                        "chat_history": chat_history_str
                    }
                    
                    guardrail_response = guardrail_chain.run(**inputs)
                    
                    # Check if clarification needed
                    if "Clarification" in guardrail_response:
                        response = guardrail_response
                        st.markdown(response)
                    else:
                        final_query = extract_query(guardrail_response)
                        st.markdown(f"**Understood Query:** {final_query}")
                        
                        # Run agent with custom callback
                        callback = StreamlitChatCallbackHandler()
                        response = agent.run(final_query, callbacks=[callback])
                        
                        st.markdown("###Final Answer")
                        st.markdown(response)
                    
                    # Add assistant response to history
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    
                except Exception as e:
                    error_msg = f"❌ Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

else:
    st.info("👈 Please upload a CSV file or select a sample dataset from the sidebar to start chatting with your data!")
    
    # Show sample datasets if available
    if sample_datasets:
        st.subheader("Available Sample Datasets")
        for name in sample_datasets.keys():
            st.write(f"- {name}")