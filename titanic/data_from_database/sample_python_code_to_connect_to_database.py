import package_name                     # package_name could be sqlite3, pymysql, pymssql

# Connect to the database ## con_str => connection string can vary
connection = package_name.connect(con_str)

cursor = package_name.cursor()              # Create the cursor

cursor.execute(query)                       # Execute query

cursor.fetchall()                           # Fetch results

connection.close()                          # Close the connection
