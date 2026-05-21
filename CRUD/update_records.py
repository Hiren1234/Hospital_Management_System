from Database.db_connection import get_connection


connection = get_connection()
cursor = connection.cursor()


query ="""UPDATE patients SET bill_amount = %s WHERE patient_id = %s"""

cursor.execute(query, (16500,2))
connection.commit()
print(f"Records updated successfully and rows affected:{cursor.rowcount}")
connection.close()