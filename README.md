# Customer Interaction Counter

## 1. Project Overview

The Customer Interaction Counter is a CRM analytics project designed to analyze customer interactions and measure customer engagement.

In a CRM system, customers interact with a business through different channels, such as Calls, Emails, Tickets, and Meetings. Tracking these interactions helps businesses understand how frequently they communicate with their customers.

This project uses Python, Pandas, and SQLite to store, process, and analyze customer interaction data. It generates an engagement report that identifies customers with low interaction levels and helps businesses decide where additional customer engagement may be required.

## 2. Project Objectives

The main objectives of this project are:

- Store customer interaction information in a structured database.
- Track interactions such as Calls, Emails, Tickets, and Meetings.
- Group interactions by customer and interaction type.
- Count the total interactions for each customer.
- Analyze customer engagement levels.
- Identify customers with low engagement.
- Generate a customer engagement report in CSV format.
- Help CRM teams make informed decisions based on interaction data.

## 3. Technologies Used

- **Python:** Used for application logic and data processing.
- **Pandas:** Used for grouping, counting, aggregation, and report generation.
- **SQLite:** Used to store customer and interaction data in a database.
- **CSV:** Used to store the input dataset and export the final engagement report.

## 4. Main Features

### 4.1 Customer Interaction Dataset

The project uses a CSV dataset containing customer interaction records.

Each record includes information such as:

- Interaction ID
- Customer ID
- Customer Name
- Interaction Type
- Interaction Date

### 4.2 Database Creation

SQLite is used to create and manage the project database.

The database stores customer interaction information in structured tables, making it easier to retrieve and analyze the data.

### 4.3 Data Loading

The project loads interaction records from the CSV dataset into the SQLite database.

This makes the data available for database queries and further analysis.

### 4.4 Interaction Counting

The system groups interaction records by customer and interaction type.

It calculates the number of Calls, Emails, Tickets, and Meetings associated with each customer.

### 4.5 Customer Engagement Analysis

The system calculates the total number of interactions for each customer and assigns an engagement level based on the configured thresholds.

The engagement categories used in the sample report are:

- **High:** Customers with a high number of interactions.
- **Medium:** Customers with a moderate number of interactions.
- **Low:** Customers with a low number of interactions.

The exact thresholds depend on the rules implemented in the analysis code.

### 4.6 Low-Engagement Customer Identification

The system identifies customers whose interaction counts fall into the Low engagement category.

This helps CRM teams identify customers who may benefit from follow-up calls, emails, meetings, or other appropriate engagement activities.

### 4.7 Engagement Report Generation

The project generates a CSV report containing customer interaction counts and engagement levels.

The report can be opened in spreadsheet applications for further review and analysis.

## 5. Project Architecture

The Customer Interaction Counter follows a simple data-processing architecture.

### 5.1 Data Layer

The data layer contains the input CSV dataset and SQLite database.

- `data/interactions.csv` stores the original interaction records.
- `database/crm.db` stores the interaction data in a structured database.

### 5.2 Processing Layer

The processing layer uses Python and Pandas to load, retrieve, group, and analyze customer interaction data.

The Python scripts in the `src/` directory handle database creation, data loading, database checking, interaction analysis, and report generation.

### 5.3 Reporting Layer

The reporting layer generates a customer engagement report in CSV format.

The report presents interaction counts and engagement categories, helping CRM teams identify customers who may require additional attention.

### Architecture Flow

Customer Interaction Dataset (CSV)

↓

Python Data Processing

↓

SQLite Database

↓

Pandas Aggregation and Grouping

↓

Customer Engagement Analysis

↓

Low-Engagement Customer Identification

↓

Customer Engagement Report (CSV)

## 6. Project Workflow

The application follows these steps:

1. **Prepare the dataset:** Store customer interaction records in `interactions.csv`.
2. **Create the database:** Create the SQLite database and required tables.
3. **Load interaction data:** Import records from the CSV file into SQLite.
4. **Check database records:** Verify that the interaction data has been loaded correctly.
5. **Analyze interactions:** Group and count interactions by customer and interaction type.
6. **Calculate engagement:** Calculate the total number of interactions for each customer.
7. **Identify low engagement:** Apply the configured engagement thresholds to identify low-engagement customers.
8. **Generate the report:** Export the customer engagement analysis to a CSV file.
9. **Review the results:** Use the report to support CRM follow-up decisions.

## 7. Project Structure

```text
CRM Project/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── interactions.csv
│
├── database/
│   └── crm.db
│
├── src/
│   ├── create_database.py
│   ├── load_data.py
│   ├── check_database.py
│   ├── analyze_interactions.py
│   └── engagement_report.py
│
├── reports/
│   └── customer_engagement_report.csv
│
└── venv/
```

**Note:** This structure reflects the project's expected files. Keep `app.py`, `requirements.txt`, or any other entries only if they exist in your actual project. The virtual environment folder (`venv/`) generally should not be committed to GitHub.

## 8. Database Design

The project uses SQLite as its database management system.

The database file is:

`database/crm.db`

The database stores customer interaction information in tables defined by the database creation script.

### Interaction Data

The interaction dataset contains the following fields:

| Field | Description |
|---|---|
| `interaction_id` | Unique identifier for an interaction |
| `customer_id` | Identifier of the customer |
| `customer_name` | Name of the customer |
| `interaction_type` | Type of interaction, such as Call, Email, Ticket, or Meeting |
| `interaction_date` | Date when the interaction occurred |

The database schema should be verified against `src/create_database.py` to ensure the documented table names and columns match the implementation.

## 9. Customer Engagement Analysis

Customer engagement is measured using the number of recorded interactions for each customer.

For example, a customer with four recorded interactions has a total interaction count of four.

The analysis groups records by customer and calculates:

- Total interactions per customer.
- Interaction counts by type.
- Engagement category based on the configured thresholds.
- A list of customers classified as Low engagement.

The engagement report generated by the project includes customers, total interaction counts, and engagement categories.

## 10. Output Report

The generated report is stored at:

`reports/customer_engagement_report.csv`

The report contains the customer engagement analysis and can be used to:

- Compare interaction levels across customers.
- Identify low-engagement customers.
- Review customer communication patterns.
- Plan suitable CRM follow-up activities.

Example results from the sample dataset:

| Customer | Total Interactions | Engagement Level |
|---|---:|---|
| Aarav Sharma | 4 | High |
| Beena Singh | 2 | Medium |
| Chahat Verma | 3 | Medium |
| Dev Kumar | 1 | Low |
| Esha Patel | 4 | High |
| Rohan Mehta | 1 | Low |

These examples reflect the sample report; the actual output depends on the dataset and configured thresholds.

## 11. How to Run the Project

### Prerequisites

Install Python 3 and ensure that `pip` is available.

### Step 1: Open the project folder

Open the `CRM Project` folder in VS Code.

### Step 2: Create a virtual environment

Run the following command in the terminal:

```bash
python3 -m venv venv
```

### Step 3: Activate the virtual environment

On macOS or Linux:

```bash
source venv/bin/activate
```

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

If the project contains a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

Otherwise, install the required packages, such as Pandas, according to the project's imports:

```bash
pip install pandas
```

SQLite is included with standard Python installations that provide the `sqlite3` module.

### Step 5: Create the database

```bash
python src/create_database.py
```

### Step 6: Load the interaction dataset

```bash
python src/load_data.py
```

### Step 7: Check the database

```bash
python src/check_database.py
```

### Step 8: Analyze customer interactions

```bash
python src/analyze_interactions.py
```

### Step 9: Generate the engagement report

```bash
python src/engagement_report.py
```

After execution, check the `reports/` directory for the generated report.

**Important:** Run the scripts in the order above only if that matches their actual dependencies. If the scripts already perform multiple steps together, follow the workflow implemented in your code.

## 12. Testing

The project can be tested using the following scenarios:

- Verify that the SQLite database and required tables are created.
- Confirm that CSV interaction records are loaded correctly.
- Check that customer and interaction details are stored accurately.
- Verify interaction counts for each customer.
- Confirm that interactions are grouped by the correct customer and type.
- Check that engagement categories follow the configured thresholds.
- Verify that low-engagement customers are correctly identified.
- Confirm that the CSV engagement report is generated successfully.
- Compare report values against the source dataset.

## 13. Business Use Case

Businesses need to maintain regular communication with their customers to understand their needs and provide appropriate support.

The Customer Interaction Counter helps CRM teams analyze recorded customer communication and identify customers with relatively low interaction levels.

For example, if a customer has very few recorded interactions compared with the configured engagement rules, the CRM team can review that customer's account and decide whether a follow-up is appropriate.

This supports data-driven customer relationship management and more organized engagement planning.

## 14. Future Enhancements

Possible future improvements include:

- Add a Streamlit dashboard for interactive data visualization.
- Display charts for interaction types and engagement categories.
- Add date-based filters for interaction analysis.
- Allow users to upload new interaction datasets.
- Add customer search functionality.
- Automate scheduled engagement report generation.
- Integrate with a live CRM system.
- Add notifications for customers who may need follow-up.
- Expand engagement analysis using interaction recency and frequency.

## 15. Conclusion

The Customer Interaction Counter is a CRM analytics project that uses Python, Pandas, and SQLite to analyze customer interactions and measure engagement levels.

It automates interaction counting, customer grouping, engagement classification, and report generation. By identifying customers with low recorded interaction levels, the system helps CRM teams make informed decisions about customer follow-up and engagement activities.

The project demonstrates practical applications of data processing, database management, aggregation, and reporting in customer relationship management.