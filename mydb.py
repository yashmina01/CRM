import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'khodia1999'
)

#preparing a cursor object
cursorObject = dataBase.cursor()

#CREATE A DATABASE
cursorObject.execute("CREATE DATABASE yashmina_01")

print("ALL DONE!!!")    