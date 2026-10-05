import sqlite3
import pandas as pd

# Connect to database
connection = sqlite3.connect("database/crm.db")

# Read interactions
query = """
SELECT
    c.customer_id,
    c.customer_name,
    i.interaction_type,
    i.interaction_date
FROM customers c
JOIN interactions i
ON c.customer_id = i.customer_id
"""

df = pd.read_sql_query(query, connection)

connection.close()

print(df)


customer_counts = df.groupby(
    ["customer_id", "customer_name"]
).size().reset_index(name="total_interactions")

print(customer_counts)


interaction_counts = df.pivot_table(
    index=["customer_id", "customer_name"],
    columns="interaction_type",
    aggfunc="size",
    fill_value=0
).reset_index()

print(interaction_counts)

interaction_types = ["Call", "Email", "Ticket", "Meeting"]

for interaction_type in interaction_types:
    if interaction_type not in interaction_counts.columns:
        interaction_counts[interaction_type] = 0


interaction_counts["Total"] = (
    interaction_counts["Call"]
    + interaction_counts["Email"]
    + interaction_counts["Ticket"]
    + interaction_counts["Meeting"]
)

interaction_counts["Total"] = (
    interaction_counts["Call"]
    + interaction_counts["Email"]
    + interaction_counts["Ticket"]
    + interaction_counts["Meeting"]
)