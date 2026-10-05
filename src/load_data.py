import sqlite3
import pandas as pd

# Read CSV file
df = pd.read_csv("data/interactions.csv")

print("CSV data loaded:")
print(df)

# Connect to database
connection = sqlite3.connect("database/crm.db")

# Get unique customers
customers = df[["customer_id", "customer_name"]].drop_duplicates()

# Insert customers into customers table
customers.to_sql(
    "customers",
    connection,
    if_exists="append",
    index=False
)

# Select interaction columns
interactions = df[
    [
        "interaction_id",
        "customer_id",
        "interaction_type",
        "interaction_date"
    ]
]

# Insert interactions into interactions table
interactions.to_sql(
    "interactions",
    connection,
    if_exists="append",
    index=False
)

# Close connection
connection.close()

print("Data loaded successfully!")