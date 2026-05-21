import pymysql

def get_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='hospital_db',




    )
    return connection
