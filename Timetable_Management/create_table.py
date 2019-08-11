import db_connect
from db_connect import *
import sqlalchemy as sa
from sqlalchemy import create_engine,text
import pymysql

def  check_table(name):
    db = db_connect()
    connection = db.connect()
    check = connection.execute('select count(*) from information_schema.tables where (table_schema = "TimeTable") and (table_name = "'+name+'")')
    check_str = check.fetchall()
    return check_str

def create_table():
    db = db_connect()
    connection = db.connect()
    print ('DATABASE CONNECTED....PERFORMING OTHER OPERATIONS')
    
    connection.execute('create table master_sem1 (Id INT NOT NULL AUTO_INCREMENT,Day varchar(30), Slot varchar(30), Location varchar(30), Batch varchar(30), Subject varchar(30), Faculty varchar(100), PRIMARY KEY (Id) )')
    connection.execute('create table master_sem2 (Id int NOT NULL AUTO_INCREMENT,Day varchar(30), Slot varchar(30), Location varchar(30), Batch varchar(30), Subject varchar(30), Faculty varchar(100), PRIMARY KEY (Id) )')
    connection.execute('create table login (Username varchar(50), Email varchar(50), Password varchar(50))')
    connection.execute('create table teacher_data (Name varchar(100), Initials varchar(10))')
    return 'Table created'
    

string = create_table()
print (string)


