# Column Descriptions Report

## Summary

- **Total Columns:** 17
- **Columns with User Descriptions:** 17
- **Categorical Columns:** 8
- **Numeric Columns:** 3
- **Datetime Columns:** 1
- **ID Columns:** 0

### Categorical Columns
- Ground
- Match_Conditions
- Team1
- Team2
- Toss_decision
- Toss_winner
- Venue
- Winner

### Numeric Columns
- First_Innings
- Match
- Second_Innings

### Datetime Columns
- Date

## Detailed Column Descriptions

### Date (Date/Time)

**User Description:** date on which the match was played

**Description:** date on which the match was played This is a date/time column. It has 5.4% missing values.

**Missing Values:** 4 (5.4%)

---

### First_Innings (Numeric)

**User Description:** runs scored in first innings

**Description:** runs scored in first innings This is a numeric column. Values range from 118 to 257, with an average of 182.7.

**Numeric Statistics:**
- **Range:** 118 to 257
- **Mean:** 182.7
- **Median:** 183.5
- **Standard Deviation:** 30.86

---

### Ground (Categorical)

**User Description:** city in which the match was played

**Description:** city in which the match was played This is a categorical column. It contains 12 unique categories. The most common value is 'Ahmedabad', appearing in approximately 12.2% of the data. Top categories include: 'Ahmedabad' (9 occurrences, 12.2%), 'Chennai' (9 occurrences, 12.2%), 'Bengaluru' (7 occurrences, 9.5%), 'Delhi' (7 occurrences, 9.5%), 'Hyderabad' (7 occurrences, 9.5%), and 5 more.

**Categorical Statistics:**
- **Unique Categories:** 12
- **Most Common Value:** 'Ahmedabad' (9 occurrences, 12.2%)

**Top Categories:**
| Category | Count | Percentage |
|---------|-------|------------|
| 'Ahmedabad' | 9 | 12.2% |
| 'Chennai' | 9 | 12.2% |
| 'Bengaluru' | 7 | 9.5% |
| 'Delhi' | 7 | 9.5% |
| 'Hyderabad' | 7 | 9.5% |
| 'Kolkata' | 7 | 9.5% |
| 'Lucknow' | 7 | 9.5% |
| 'Mumbai' | 7 | 9.5% |
| 'Jaipur' | 5 | 6.8% |
| 'Mohali' | 5 | 6.8% |

---

### MOM (object)

**User Description:** man of the match

**Description:** man of the match This is a object column.

---

### Match (Numeric)

**User Description:** shows match sequence number

**Description:** shows match sequence number This is a numeric column. Values range from 1 to 70, with an average of 34.56.

**Missing Values:** 2 (2.7%)

**Numeric Statistics:**
- **Range:** 1 to 70
- **Mean:** 34.56
- **Median:** 34.50
- **Standard Deviation:** 20.84

---

### Match_Conditions (Categorical)

**User Description:** whether it was Day/Night or Night match

**Description:** whether it was Day/Night or Night match This is a categorical column. It contains 2 unique categories. The most common value is 'Night', appearing in approximately 75.7% of the data. Top categories include: 'Night' (56 occurrences, 75.7%), 'Day/Night' (18 occurrences, 24.3%).

**Categorical Statistics:**
- **Unique Categories:** 2
- **Most Common Value:** 'Night' (56 occurrences, 75.7%)

**Top Categories:**
| Category | Count | Percentage |
|---------|-------|------------|
| 'Night' | 56 | 75.7% |
| 'Day/Night' | 18 | 24.3% |

---

### Result (object)

**User Description:** result in words

**Description:** result in words This is a object column.

---

### Second_Innings (Numeric)

**User Description:** runs scored in second innings

**Description:** runs scored in second innings This is a numeric column. Values range from 0 to 218, with an average of 164.4. It contains some outlier values.

**Numeric Statistics:**
- **Range:** 0 to 218
- **Mean:** 164.4
- **Median:** 171
- **Standard Deviation:** 36.54
- **Contains outliers**

---

### Team1 (Categorical)

**User Description:** team 1

**Description:** team 1 This is a categorical column. It contains 10 unique categories. The most common value is 'Chennai Super Kings', appearing in approximately 13.5% of the data. Top categories include: 'Chennai Super Kings' (10 occurrences, 13.5%), 'Delhi Capitals' (10 occurrences, 13.5%), 'Gujarat Titans' (10 occurrences, 13.5%), 'Lucknow Super Giants' (10 occurrences, 13.5%), 'Kolkata Knight Riders' (8 occurrences, 10.8%), and 5 more.

**Categorical Statistics:**
- **Unique Categories:** 10
- **Most Common Value:** 'Chennai Super Kings' (10 occurrences, 13.5%)

**Top Categories:**
| Category | Count | Percentage |
|---------|-------|------------|
| 'Chennai Super Kings' | 10 | 13.5% |
| 'Delhi Capitals' | 10 | 13.5% |
| 'Gujarat Titans' | 10 | 13.5% |
| 'Lucknow Super Giants' | 10 | 13.5% |
| 'Kolkata Knight Riders' | 8 | 10.8% |
| 'Mumbai Indians' | 7 | 9.5% |
| 'Punjab Kings' | 6 | 8.1% |
| 'Rajasthan Royals' | 5 | 6.8% |
| 'Sunrisers Hyderabad' | 5 | 6.8% |
| 'Royal Challengers Bangalore' | 3 | 4.1% |

---

### Team2 (Categorical)

**User Description:** team 2

**Description:** team 2 This is a categorical column. It contains 10 unique categories. The most common value is 'Royal Challengers Bangalore', appearing in approximately 14.9% of the data. Top categories include: 'Royal Challengers Bangalore' (11 occurrences, 14.9%), 'Mumbai Indians' (9 occurrences, 12.2%), 'Rajasthan Royals' (9 occurrences, 12.2%), 'Sunrisers Hyderabad' (9 occurrences, 12.2%), 'Punjab Kings' (8 occurrences, 10.8%), and 5 more.

**Categorical Statistics:**
- **Unique Categories:** 10
- **Most Common Value:** 'Royal Challengers Bangalore' (11 occurrences, 14.9%)

**Top Categories:**
| Category | Count | Percentage |
|---------|-------|------------|
| 'Royal Challengers Bangalore' | 11 | 14.9% |
| 'Mumbai Indians' | 9 | 12.2% |
| 'Rajasthan Royals' | 9 | 12.2% |
| 'Sunrisers Hyderabad' | 9 | 12.2% |
| 'Punjab Kings' | 8 | 10.8% |
| 'Gujarat Titans' | 7 | 9.5% |
| 'Chennai Super Kings' | 6 | 8.1% |
| 'Kolkata Knight Riders' | 6 | 8.1% |
| 'Lucknow Super Giants' | 5 | 6.8% |
| 'Delhi Capitals' | 4 | 5.4% |

---

### Teams (object)

**User Description:** teams between whom the match was played

**Description:** teams between whom the match was played This is a object column.

---

### Toss (category)

**User Description:** who won the toss and what they opted

**Description:** who won the toss and what they opted This is a category column.

---

### Toss_decision (Categorical)

**User Description:** what they opted

**Description:** what they opted This is a categorical column. It contains 2 unique categories. The most common value is 'Bowl', appearing in approximately 71.6% of the data. Top categories include: 'Bowl' (53 occurrences, 71.6%), 'Bat' (21 occurrences, 28.4%).

**Categorical Statistics:**
- **Unique Categories:** 2
- **Most Common Value:** 'Bowl' (53 occurrences, 71.6%)

**Top Categories:**
| Category | Count | Percentage |
|---------|-------|------------|
| 'Bowl' | 53 | 71.6% |
| 'Bat' | 21 | 28.4% |

---

### Toss_winner (Categorical)

**User Description:** team who won the toss

**Description:** team who won the toss This is a categorical column. It contains 10 unique categories. The most common value is 'Chennai Super Kings', appearing in approximately 13.5% of the data. Top categories include: 'Chennai Super Kings' (10 occurrences, 13.5%), 'Mumbai Indians' (10 occurrences, 13.5%), 'Rajasthan Royals' (10 occurrences, 13.5%), 'Gujarat Titans' (9 occurrences, 12.2%), 'Royal Challengers Bangalore' (8 occurrences, 10.8%), and 5 more.

**Categorical Statistics:**
- **Unique Categories:** 10
- **Most Common Value:** 'Chennai Super Kings' (10 occurrences, 13.5%)

**Top Categories:**
| Category | Count | Percentage |
|---------|-------|------------|
| 'Chennai Super Kings' | 10 | 13.5% |
| 'Mumbai Indians' | 10 | 13.5% |
| 'Rajasthan Royals' | 10 | 13.5% |
| 'Gujarat Titans' | 9 | 12.2% |
| 'Royal Challengers Bangalore' | 8 | 10.8% |
| 'Delhi Capitals' | 7 | 9.5% |
| 'Sunrisers Hyderabad' | 7 | 9.5% |
| 'Kolkata Knight Riders' | 5 | 6.8% |
| 'Punjab Kings' | 5 | 6.8% |
| 'Lucknow Super Giants' | 3 | 4.1% |

---

### Venue (Categorical)

**User Description:** exact name of the ground

**Description:** exact name of the ground This is a categorical column. It contains 12 unique categories. The most common value is 'MA Chidambaram Stadium', appearing in approximately 12.2% of the data. Top categories include: 'MA Chidambaram Stadium' (9 occurrences, 12.2%), 'Narendra Modi Stadium' (9 occurrences, 12.2%), 'Arun Jaitley Stadium' (7 occurrences, 9.5%), 'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium' (7 occurrences, 9.5%), 'Eden Gardens' (7 occurrences, 9.5%), and 5 more.

**Categorical Statistics:**
- **Unique Categories:** 12
- **Most Common Value:** 'MA Chidambaram Stadium' (9 occurrences, 12.2%)

**Top Categories:**
| Category | Count | Percentage |
|---------|-------|------------|
| 'MA Chidambaram Stadium' | 9 | 12.2% |
| 'Narendra Modi Stadium' | 9 | 12.2% |
| 'Arun Jaitley Stadium' | 7 | 9.5% |
| 'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium' | 7 | 9.5% |
| 'Eden Gardens' | 7 | 9.5% |
| 'M.Chinnaswamy Stadium' | 7 | 9.5% |
| 'Rajiv Gandhi International Stadium' | 7 | 9.5% |
| 'Wankhede Stadium' | 7 | 9.5% |
| 'Punjab Cricket Association IS Bindra Stadium' | 5 | 6.8% |
| 'Sawai Mansingh Stadium' | 5 | 6.8% |

---

### Winner (Categorical)

**User Description:** which team won

**Description:** which team won This is a categorical column. It contains 11 unique categories. The most common value is 'Gujarat Titans', appearing in approximately 14.9% of the data. Top categories include: 'Gujarat Titans' (11 occurrences, 14.9%), 'Chennai Super Kings' (10 occurrences, 13.5%), 'Mumbai Indians' (9 occurrences, 12.2%), 'Lucknow Super Giants' (8 occurrences, 10.8%), 'Rajasthan Royals' (7 occurrences, 9.5%), and 5 more.

**Categorical Statistics:**
- **Unique Categories:** 11
- **Most Common Value:** 'Gujarat Titans' (11 occurrences, 14.9%)

**Top Categories:**
| Category | Count | Percentage |
|---------|-------|------------|
| 'Gujarat Titans' | 11 | 14.9% |
| 'Chennai Super Kings' | 10 | 13.5% |
| 'Mumbai Indians' | 9 | 12.2% |
| 'Lucknow Super Giants' | 8 | 10.8% |
| 'Rajasthan Royals' | 7 | 9.5% |
| 'Royal Challengers Bangalore' | 7 | 9.5% |
| 'Kolkata Knight Riders' | 6 | 8.1% |
| 'Punjab Kings' | 6 | 8.1% |
| 'Delhi Capitals' | 5 | 6.8% |
| 'Sunrisers Hyderabad' | 4 | 5.4% |

---

### Won_by (object)

**User Description:** margin of victory

**Description:** margin of victory This is a object column.

---
