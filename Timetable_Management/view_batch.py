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

def view_batch(grade):
    Main = []
    cell_1 = gen_batch (grade,'1')
    Main = []
    Main.append('1')
    for key,val in cell_1.items():
        S1 = val
        Main.append(S1)
    
    cell_2 = gen_batch (grade,'2')
    Main.append('2')
    for key,val in cell_2.items():
        S1 = val
        Main.append(S1)
    
    cell_3 = gen_batch (grade,'3')
    Main.append('3')
    for key,val in cell_3.items():
        S1 = val
        Main.append(S1)
    
    cell_4 = gen_batch (grade,'4')
    Main.append('4')
    for key,val in cell_4.items():
        S1 = val
        Main.append(S1)
    
    cell_5 = gen_batch (grade,'5')
    Main.append('5')
    for key,val in cell_5.items():
        S1 = val
        Main.append(S1)
    
    cell_6 = gen_batch (grade,'6')
    Main.append('6')
    for key,val in cell_6.items():
        S1 = val
        Main.append(S1)
    
    cell_7 = gen_batch (grade,'7')
    Main.append('7')
    for key,val in cell_7.items():
        S1 = val
        Main.append(S1)
    
    cell_8 = gen_batch (grade,'8')
    Main.append('8')
    for key,val in cell_8.items():
        S1 = val
        Main.append(S1)
    
    return Main
     


def gen_batch(grade , slot):
    db = db_connect()
    connection = db.connect()
    print (grade)
    #teachername = input('ENTER TEACHER NAME :')
    sql_user = "select Day,Slot,Batch,Location,Subject,Faculty from master_sem1 where Batch REGEXP '"+grade+"' and Slot = '"+slot+"'"
    user_result = connection.execute(sql_user)
    user_res = user_result.fetchall()
    user_res_str = str(user_res)
    #print (user_res)
    #print (user_result)
    mond = []
    tues = []
    wed  = []
    thur = []
    fri  = []
    sat  = []
    cell_1 = {
        "Monday" : "",
        "Tuesday" : "",
        "Wednesday" : "",
        "Thursday" : "",
        "Friday" : "",
        "Saturday" : ""
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
                mond.append(ce)
                #test = {"Monday" : ce}
                #cell_1['Monday'].append(ce)
            elif Da == 'Tuesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                tues.append(ce)
                #test = {"Tuesday" : ce}
                #cell_1['Tuesday'].append(ce)
            elif Da == 'Wednesday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                wed.append(ce)
                #test = {"Wednesday" : ce}
                #cell_1['Wednesday'].append(ce)
            elif Da == 'Thursday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                thur.append(ce)
                #test = {"Thursday" : ce}
                #cell_1['Thursday'].append(ce)
            elif Da == 'Friday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                fri.append(ce)
                #test = {"Friday" : ce}
                #cell_1['Friday'].append(ce)
            elif Da == 'Saturday':
                ce = Su+" - "+Ba+" - ("+Fa+") - "+Lo
                sat.append(ce)
                #test = {"Saturday" : ce}
                #cell_1['Saturday'].append(ce)
    else:
        print ('No teacher')

    monday_1 = ''
    tuesday_1 = ''
    wednesday_1 = ''
    thursday_1 = ''
    friday_1 = ''
    saturday_1 = ''
    
    
    for x in mond:
        monday_1 += x
        monday_1 += ' || '
    print (mond)
    print (monday_1)
    test = {'Monday' : monday_1}
    cell_1.update(test)

    for x in tues:
        tuesday_1 += x
        tuesday_1 += ' || '
    print (tues)
    print (tuesday_1)
    test = {'Tuesday' : tuesday_1}
    cell_1.update(test)

    for x in wed:
        wednesday_1 += x
        wednesday_1 += ' || '
    print (wed)
    print (wednesday_1)
    test = {'Wednesday' : wednesday_1}
    cell_1.update(test)
    
    for x in thur:
        thursday_1 += x
        thursday_1 += ' || '
    print (thur)
    print (thursday_1)
    test = {'Thursday' : thursday_1}
    cell_1.update(test)

    for x in fri:
        friday_1 += x
        friday_1 += ' || '
    print (fri)
    print (friday_1)
    test = {'Friday' : friday_1}
    cell_1.update(test)

    for x in sat:
        saturday_1 += x
        saturday_1 += ' || '
    print (sat)
    print (saturday_1)
    test = {'Saturday' : saturday_1}
    cell_1.update(test)

    return cell_1