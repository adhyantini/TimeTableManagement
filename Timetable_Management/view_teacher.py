import sqlalchemy
from sqlalchemy import create_engine,text
import pymysql
import json
from flask import jsonify
#-- Connect To Db
def db_connect():
    engine = create_engine('mysql+pymysql://root1:password@localhost/TimeTable')
    # Create a Cursor object to execute queries.
    print ('Connected To Database')
    return engine


def view_teacher(teachername):
    db = db_connect()
    connection = db.connect()
    #teachername = input('ENTER TEACHER NAME :')
    sql_user = "select Day,Slot,Location,Batch,Subject,Faculty from master_sem1 where faculty = '"+teachername+"' and Slot = '1'"
    user_result = connection.execute(sql_user)
    user_res = user_result.fetchall()
    user_res_str = str(user_res)
    #print (user_res)
    #print (user_result)

    cell_1 = {
        "Monday" : "NULL",
        "Tuesday" : "NULL",
        "Wednesday" : "NULL",
        "Thursday" : "NULL",
        "Friday" : "NULL",
        "Saturday" : "NULL"
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
            if Da == 'Monday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Monday" : ce}
                cell_1.update(test)
            elif Da == 'Tuesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Tuesday" : ce}
                cell_1.update(test)
            elif Da == 'Wednesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Wednesday" : ce}
                cell_1.update(test)
            elif Da == 'Thursday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Thursday" : ce}
                cell_1.update(test)
            elif Da == 'Friday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Friday" : ce}
                cell_1.update(test)
            elif Da == 'Saturday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Saturday" : ce}
                cell_1.update(test)
    else:
        print ('No teacher')


    sql_user = "select Day,Slot,Location,Batch,Subject,Faculty from master_sem1 where faculty = '"+teachername+"' and Slot = '2'"
    user_result = connection.execute(sql_user)
    user_res = user_result.fetchall()
    user_res_str = str(user_res)
    #print (user_res)
    #print (user_result)

    cell_2 = {
        "Monday" : "NULL",
        "Tuesday" : "NULL",
        "Wednesday" : "NULL",
        "Thursday" : "NULL",
        "Friday" : "NULL",
        "Saturday" : "NULL"
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
            if Da == 'Monday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Monday" : ce}
                cell_2.update(test)
            elif Da == 'Tuesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Tuesday" : ce}
                cell_2.update(test)
            elif Da == 'Wednesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Wednesday" : ce}
                cell_2.update(test)
            elif Da == 'Thursday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Thursday" : ce}
                cell_2.update(test)
            elif Da == 'Friday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Friday" : ce}
                cell_2.update(test)
            elif Da == 'Saturday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Saturday" : ce}
                cell_2.update(test)
    else:
        print ('No teacher')


    sql_user = "select Day,Slot,Location,Batch,Subject,Faculty from master_sem1 where faculty = '"+teachername+"' and Slot = '3'"
    user_result = connection.execute(sql_user)
    user_res = user_result.fetchall()
    user_res_str = str(user_res)
    #print (user_res)
    #print (user_result)

    cell_3 = {
        "Monday" : "NULL",
        "Tuesday" : "NULL",
        "Wednesday" : "NULL",
        "Thursday" : "NULL",
        "Friday" : "NULL",
        "Saturday" : "NULL"
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
            if Da == 'Monday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Monday" : ce}
                cell_3.update(test)
            elif Da == 'Tuesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Tuesday" : ce}
                cell_3.update(test)
            elif Da == 'Wednesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Wednesday" : ce}
                cell_3.update(test)
            elif Da == 'Thursday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Thursday" : ce}
                cell_3.update(test)
            elif Da == 'Friday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Friday" : ce}
                cell_3.update(test)
            elif Da == 'Saturday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Saturday" : ce}
                cell_3.update(test)
    else:
        print ('No teacher')


    sql_user = "select Day,Slot,Location,Batch,Subject,Faculty from master_sem1 where faculty = '"+teachername+"' and Slot = '4'"
    user_result = connection.execute(sql_user)
    user_res = user_result.fetchall()
    user_res_str = str(user_res)
    #print (user_res)
    #print (user_result)

    cell_4 = {
        "Monday" : "NULL",
        "Tuesday" : "NULL",
        "Wednesday" : "NULL",
        "Thursday" : "NULL",
        "Friday" : "NULL",
        "Saturday" : "NULL"
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
            if Da == 'Monday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Monday" : ce}
                cell_4.update(test)
            elif Da == 'Tuesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Tuesday" : ce}
                cell_4.update(test)
            elif Da == 'Wednesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Wednesday" : ce}
                cell_4.update(test)
            elif Da == 'Thursday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Thursday" : ce}
                cell_4.update(test)
            elif Da == 'Friday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Friday" : ce}
                cell_4.update(test)
            elif Da == 'Saturday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Saturday" : ce}
                cell_4.update(test)
    else:
        print ('No teacher')

    sql_user = "select Day,Slot,Location,Batch,Subject,Faculty from master_sem1 where faculty = '"+teachername+"' and Slot = '5'"
    user_result = connection.execute(sql_user)
    user_res = user_result.fetchall()
    user_res_str = str(user_res)
    #print (user_res)
    #print (user_result)

    cell_5 = {
        "Monday" : "NULL",
        "Tuesday" : "NULL",
        "Wednesday" : "NULL",
        "Thursday" : "NULL",
        "Friday" : "NULL",
        "Saturday" : "NULL"
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
            if Da == 'Monday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Monday" : ce}
                cell_5.update(test)
            elif Da == 'Tuesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Tuesday" : ce}
                cell_5.update(test)
            elif Da == 'Wednesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Wednesday" : ce}
                cell_5.update(test)
            elif Da == 'Thursday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Thursday" : ce}
                cell_5.update(test)
            elif Da == 'Friday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Friday" : ce}
                cell_5.update(test)
            elif Da == 'Saturday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Saturday" : ce}
                cell_5.update(test)
    else:
        print ('No teacher')


    sql_user = "select Day,Slot,Location,Batch,Subject,Faculty from master_sem1 where faculty = '"+teachername+"' and Slot = '6'"
    user_result = connection.execute(sql_user)
    user_res = user_result.fetchall()
    user_res_str = str(user_res)
    #print (user_res)
    #print (user_result)

    cell_6 = {
        "Monday" : "NULL",
        "Tuesday" : "NULL",
        "Wednesday" : "NULL",
        "Thursday" : "NULL",
        "Friday" : "NULL",
        "Saturday" : "NULL"
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
            if Da == 'Monday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Monday" : ce}
                cell_6.update(test)
            elif Da == 'Tuesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Tuesday" : ce}
                cell_6.update(test)
            elif Da == 'Wednesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Wednesday" : ce}
                cell_6.update(test)
            elif Da == 'Thursday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Thursday" : ce}
                cell_6.update(test)
            elif Da == 'Friday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Friday" : ce}
                cell_6.update(test)
            elif Da == 'Saturday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Saturday" : ce}
                cell_6.update(test)
    else:
        print ('No teacher')


    sql_user = "select Day,Slot,Location,Batch,Subject,Faculty from master_sem1 where faculty = '"+teachername+"' and Slot = '7'"
    user_result = connection.execute(sql_user)
    user_res = user_result.fetchall()
    user_res_str = str(user_res)
    #print (user_res)
    #print (user_result)

    cell_7 = {
        "Monday" : "NULL",
        "Tuesday" : "NULL",
        "Wednesday" : "NULL",
        "Thursday" : "NULL",
        "Friday" : "NULL",
        "Saturday" : "NULL"
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
            if Da == 'Monday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Monday" : ce}
                cell_7.update(test)
            elif Da == 'Tuesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Tuesday" : ce}
                cell_7.update(test)
            elif Da == 'Wednesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Wednesday" : ce}
                cell_7.update(test)
            elif Da == 'Thursday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Thursday" : ce}
                cell_7.update(test)
            elif Da == 'Friday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Friday" : ce}
                cell_7.update(test)
            elif Da == 'Saturday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Saturday" : ce}
                cell_7.update(test)
    else:
        print ('No teacher')


    sql_user = "select Day,Slot,Location,Batch,Subject,Faculty from master_sem1 where faculty = '"+teachername+"' and Slot = '8'"
    user_result = connection.execute(sql_user)
    user_res = user_result.fetchall()
    user_res_str = str(user_res)
    #print (user_res)
    #print (user_result)

    cell_8 = {
        "Monday" : "NULL",
        "Tuesday" : "NULL",
        "Wednesday" : "NULL",
        "Thursday" : "NULL",
        "Friday" : "NULL",
        "Saturday" : "NULL"
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
            if Da == 'Monday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Monday" : ce}
                cell_8.update(test)
            elif Da == 'Tuesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Tuesday" : ce}
                cell_8.update(test)
            elif Da == 'Wednesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Wednesday" : ce}
                cell_8.update(test)
            elif Da == 'Thursday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Thursday" : ce}
                cell_8.update(test)
            elif Da == 'Friday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Friday" : ce}
                cell_8.update(test)
            elif Da == 'Saturday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                test = {"Saturday" : ce}
                cell_8.update(test)
    else:
        print ('No teacher')

    Main = []
    Main.append('1')
    for key,val in cell_1.items():
        S1 = val
        Main.append(S1)
    Main.append('2')
    for key,val in cell_2.items():
        S1 = val
        Main.append(S1)
    Main.append('3')
    for key,val in cell_3.items():
        S1 = val
        Main.append(S1)
    Main.append('4')
    for key,val in cell_4.items():
        S1 = val
        Main.append(S1)
    Main.append('5')
    for key,val in cell_5.items():
        S1 = val
        Main.append(S1)
    Main.append('6')
    for key,val in cell_6.items():
        S1 = val
        Main.append(S1)
    Main.append('7')
    for key,val in cell_7.items():
        S1 = val
        Main.append(S1)
    Main.append('8')
    for key,val in cell_8.items():
        S1 = val
        Main.append(S1)
    '''Slot_2 = json.dumps(cell_2)
    Slot_3 = json.dumps(cell_3)
    Slot_4 = json.dumps(cell_4)
    Slot_5 = json.dumps(cell_5)
    Slot_6 = json.dumps(cell_6)
    Slot_7 = json.dumps(cell_7)
    Slot_8 = json.dumps(cell_8)'''
    return Main
    #load_Slot1 = json.loads(Slot_1)
    #print (Slot_1)
    '''Main = {
        "1" : Slot_1,
        "2" : Slot_2,
        "3" : Slot_3,
        "4" : Slot_4,
        "5" : Slot_5,
        "6" : Slot_6,
        "7" : Slot_7,
        "8" : Slot_8,
    }
    print (Main)'''


'''    Slot_1 = json.dumps(cell_1)
    Slot_2 = json.dumps(cell_2)
    Slot_3 = json.dumps(cell_3)
    Slot_4 = json.dumps(cell_4)
    Slot_5 = json.dumps(cell_5)
    Slot_6 = json.dumps(cell_6)
    Slot_7 = json.dumps(cell_7)
    Slot_8 = json.dumps(cell_8)
    load_Slot1 = json.loads(Slot_1)
    load_Slot2 = json.loads(Slot_2)
    load_Slot3 = json.loads(Slot_3)
    load_Slot4 = json.loads(Slot_4)
    load_Slot5 = json.loads(Slot_5)
    load_Slot6 = json.loads(Slot_6)
    load_Slot7 = json.loads(Slot_7)
    load_Slot8 = json.loads(Slot_8)
    
    #print (load_Slot1)
    Main = {
        "1" : Slot_1,
        "2" : Slot_2,
        "3" : Slot_3,
        "4" : Slot_4,
        "5" : Slot_5,
        "6" : Slot_6,
        "7" : Slot_7,
        "8" : Slot_8,
    }

    Main_Load = {
        "1" : load_Slot1,
        "2" : load_Slot2,
        "3" : load_Slot3,
        "4" : load_Slot4,
        "5" : load_Slot5,
        "6" : load_Slot6,
        "7" : load_Slot7,
        "8" : load_Slot8,
        }
    #print (Main_Load)
    #print (load_Slot1)
    return Main_Load'''