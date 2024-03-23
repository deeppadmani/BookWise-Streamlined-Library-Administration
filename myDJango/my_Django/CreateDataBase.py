import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Deep@1313'
)


Obj = dataBase.cursor()
Obj.execute("create database IF NOT EXISTS library")
Obj.execute("use library")

