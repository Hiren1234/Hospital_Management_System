from Database.db_connection import get_connection

connection = get_connection()
cursor = connection.cursor()
print("Connection has been established")

query ="""INSERT INTO patients
(patient_name, age, gender, disease,doctor_name, admission_date, discharge_date, bill_amount)
values(%s,%s,%s,%s,%s,%s,%s,%s)
"""

records = [
    ("Rahul Patel", 35, "Male", "Fever", "Dr.Patel", "2026-05-01","2026-05-05", 12000),
    ("Priyal Patel", 28, "Female","Blood Cancer", "Dr.Shah", "2026-05-03","2026-05-08",18000),
    ("Amit Verma", 40, "Male","Heart Disease", "Dr.Rao", "2026-05-02", "2026-05-10", 75000)
]

cursor.executemany(query, records)
connection.commit()
print("Bulk records has been inserted")
connection.close()


