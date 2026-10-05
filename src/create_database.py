import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("database/crm.db")

# Create cursor
cursor = connection.cursor()

# Create customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT NOT NULL
)
""")

# Create interactions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interactions (
    interaction_id INTEGER PRIMARY KEY,
    customer_id TEXT,
    interaction_type TEXT,
    interaction_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

# Save changes
connection.commit()

# Close database connection
connection.close()

print("Database and tables created successfully!")