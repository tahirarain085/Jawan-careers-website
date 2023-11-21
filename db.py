import mysql.connector

# Create a connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ilovepakistan",
    database="jawancareers"
)