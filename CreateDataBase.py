import mysql.connector


dataBase = mysql.connector.connect(
    host = 'db',
    user = 'root',
    passwd = 'Deep@1313'
)
print("Executing CreateDataBase.py script...")

Obj = dataBase.cursor()
Obj.execute("create database IF NOT EXISTS library")
Obj.execute("use library")

