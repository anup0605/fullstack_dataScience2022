import mysql.connector as conn
from flask import Flask

app = Flask(__name__)
mydb = conn.connect(host="localhost", user="root", password="mysql0605")
# print(mydb.isConnected())
cursor = mydb.cursor()
# cursor.execute("create database if not exist MicroTalk")
# cursor.execute("create table if not exist MicroTalk.employee(name varchar(30), number int)")
# cursor.execute("show databases")

