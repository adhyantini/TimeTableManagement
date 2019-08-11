import sqlalchemy
from sqlalchemy import create_engine,text
import pymysql
import json
from flask import jsonify

def db_connect():
    engine = create_engine('mysql+pymysql://root1:password@localhost/TimeTable')
    # Create a Cursor object to execute queries.
    print ('Connected To Database')
    return engine

def Master(time,s):
    """ Returns data of master timetable o be displayed on screen in format 'location:Subject-Batch-Faculty' """	
    db = db_connect()
    connection = db.connect()
    master_sem1 = 'master_sem1'
    #teachername = input('ENTER TEACHER NAME :')
    sql_user = "Select Day,Slot,Location,Batch,Subject,Faculty from "+master_sem1+" where Day = '"+time+"' and Slot = '"+s+"'"
    user_result = connection.execute(sql_user)
    user_res = user_result.fetchall()
    user_res_str = str(user_res)
    #print (user_res)
    #print (user_result)

    monday_1 = {
        "SL1" : "",
        "SL2" : "",
        "SysL" : "",
        "HL" : "",
        "PR" : "",
        "PL" : "",
	    "ONL1" : "",
	    "ONL2" : "",
	    "ONL3" : "",
	    "PGL" : "",
	    "422" : "",
	    "424" : "",
	    "320" : "",
	    "325" : "",
	    "420B" : ""

       }
    #-- Check if Public-Key is Present
    if len(user_res_str) != 2:
        print ('Data Present!')
        for row in user_res:
            Sl = row['Slot']
            Da = row['Day']
            Lo = row['Location']
            Ba = row['Batch']
            Su = row['Subject']
            Fa = row['Faculty']
            if Lo == 'SL1':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"SL1" : ce}
                monday_1.update(test)
            elif Lo == 'SL2':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"SL2" : ce}
                monday_1.update(test)
            elif Lo == 'SysL':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"SysL" : ce}
                monday_1.update(test)
            elif Lo == 'HL':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"HL" : ce}
                monday_1.update(test)
            elif Lo == 'PR':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"PR" : ce}
                monday_1.update(test)
            elif Lo == 'PL':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"PL" : ce}
                monday_1.update(test)
            elif Lo == 'ONL1':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"ONL1" : ce}
                monday_1.update(test)
            elif Lo == 'ONL2':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"ONL2" : ce}
                monday_1.update(test)
            elif Lo == 'ONL3':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"ONL3" : ce}
                monday_1.update(test)
            elif Lo == 'PGL':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"PGL" : ce}
                monday_1.update(test)
            elif Lo == '422':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"422" : ce}
                monday_1.update(test)
            elif Lo == '424':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"424" : ce}
                monday_1.update(test)
            elif Lo == '320':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"320" : ce}
                monday_1.update(test)
            elif Lo == '325':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"325" : ce}
                monday_1.update(test)
            elif Lo == '420B':
                ce = Su+" - "+Ba+" - ("+Fa+")"
                test = {"420B" : ce}
                monday_1.update(test)
            

    else:
        print ('No Subject Data')

    return monday_1
