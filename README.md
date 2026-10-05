# Customer Interaction Counter

## Project Objective

The Customer Interaction Counter is a CRM analytics project that analyzes customer interactions such as Calls, Emails, Tickets, and Meetings.

The system counts interactions for each customer and identifies customers with low engagement.

## Technologies Used

- Python
- pandas
- SQLite
- Data aggregation and grouping

## Project Workflow

Customer Interactions
↓
Group by Customer and Interaction Type
↓
Count Interactions
↓
Analyze Customer Engagement
↓
Identify Low-Engagement Customers
↓
Suggest CRM Action

## Project Structure

```text
CRM Project/
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
├── venv/
│
└── README.md