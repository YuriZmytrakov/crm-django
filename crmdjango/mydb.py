import mysql.connector

# Establish connection to the MySQL server
dataBase = mysql.connector.connect(
    host='localhost',
    user='yuri',
    passwd='password123',
) 

# Create a cursor object to execute SQL queries
cursorObject = dataBase.cursor()

# Execute SQL query to create a new database named "elderco"
cursorObject.execute("CREATE DATABASE elderco")

# Close cursor and database connection
cursorObject.close()
dataBase.close()

print("Database 'elderco' created successfully!")
