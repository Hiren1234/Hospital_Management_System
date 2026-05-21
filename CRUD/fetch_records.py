# Here I will perform read operations
import pandas as pd
from Database.db_connection import get_connection

connection = get_connection()
print(connection,"has been established")

query = "SELECT * FROM patients"

df = pd.read_sql(query,connection)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print(df)

connection.close()

