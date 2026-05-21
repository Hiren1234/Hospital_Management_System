from Database.db_connection import get_connection


connection = get_connection()

cursor = connection.cursor()

query ="DELETE FROM patients WHERE patient_id =%s"

cursor.execute(query, (3,))
connection.commit()
print(f"{cursor.rowcount} records deleted")
connection.close()





