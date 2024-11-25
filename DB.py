import pyodbc

# Define the connection string
conn_str = (
    r'DRIVER={ODBC Driver 18 for SQL Server};'
    r'SERVER=DESKTOP-8I403LG;'  # Change to your server and instance name
    r'DATABASE=DemoDB;'        # Change to your database name
    r'UID=your_username;'                  # Change to your username
    r'PWD=your_password'                   # Change to your password
)

# Establish the connection
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Example query
cursor.execute("SELECT * from payment;")
# row = cursor.fetchone()
# print(row)

# Close the connection
cursor.close()
conn.close()
