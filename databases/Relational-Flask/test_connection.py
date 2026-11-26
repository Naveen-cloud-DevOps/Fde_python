import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='dev'
    )

    print("MySQL Connected Successfully!")

    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE()")

    print("Database:", cursor.fetchone())

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print("MySQL Connection Failed:", err)