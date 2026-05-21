from Database.db_connection import get_connection
import pandas as pd

connection = get_connection()
cursor = connection.cursor()

df = pd.read_sql("SELECT * FROM patients", connection)
print(df)

df.drop_duplicates(inplace=True)

df.fillna(0,inplace=True)
# Convert col names to lower case
df.columns = df.columns.str.lower()

# Remove extra spaces
df["patient_name"] = df["patient_name"].str.strip()

# Filtering negative billing amount
df= df[df["bill_amount"]>0]

print(df)

# Now Performing Data Maniulation
print("\n Highest Bill Amount or sorting")
df.sort_values(by="bill_amount", ascending=False, inplace=True)
print(df)


# Find Average Bill
print("\n Average Bill Amount")
average_bill = df["bill_amount"].mean()
print(average_bill)

print("\n Average Bill Amount by Diseases")
# Group by disease
grouped = df.groupby("disease")["bill_amount"].mean()
print(grouped)

print("\n Filter High Bill Patient")
high_bill = df[df["bill_amount"]>13000]
print(high_bill)


