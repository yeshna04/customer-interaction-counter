import sqlite3
import pandas as pd

connection = sqlite3.connect("database/crm.db")

query = "SELECT * FROM interactions"

df = pd.read_sql_query(query, connection)

print(df)

connection.close()