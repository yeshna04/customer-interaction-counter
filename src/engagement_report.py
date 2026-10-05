import sqlite3
import pandas as pd

# Connect to database
connection = sqlite3.connect("database/crm.db")

# Get customer interaction data
query = """
SELECT
    c.customer_id,
    c.customer_name,
    i.interaction_type
FROM customers c
JOIN interactions i
ON c.customer_id = i.customer_id
"""

df = pd.read_sql_query(query, connection)

connection.close()

# Count interaction types
report = df.pivot_table(
    index=["customer_id", "customer_name"],
    columns="interaction_type",
    aggfunc="size",
    fill_value=0
).reset_index()

# Make sure all interaction types exist
interaction_types = ["Call", "Email", "Ticket", "Meeting"]

for interaction_type in interaction_types:
    if interaction_type not in report.columns:
        report[interaction_type] = 0

# Calculate total interactions
report["Total_Interactions"] = (
    report["Call"]
    + report["Email"]
    + report["Ticket"]
    + report["Meeting"]
)

# Calculate engagement level
def get_engagement_level(total):
    if total <= 1:
        return "Low"
    elif total <= 3:
        return "Medium"
    else:
        return "High"

report["Engagement_Level"] = report["Total_Interactions"].apply(
    get_engagement_level
)

print(report)

low_engagement = report[
    report["Engagement_Level"] == "Low"
]

print("\nLow Engagement Customers:")
print(low_engagement)


def get_crm_action(level):
    if level == "Low":
        return "Follow-up Required"
    elif level == "Medium":
        return "Monitor Engagement"
    else:
        return "Engagement Healthy"


report["CRM_Action"] = report["Engagement_Level"].apply(
    get_crm_action
)


report.to_csv(
    "reports/customer_engagement_report.csv",
    index=False
)

print("\nReport saved successfully!")