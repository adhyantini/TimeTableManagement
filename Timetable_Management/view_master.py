import sqlalchemy
from sqlalchemy import create_engine,text
import pymysql
import json
import master_data
from master_data import *
from flask import jsonify

#-- Connect To Db



def view_master():
    Main = []
    monday_1 = Master('Monday', '1')
    
    #Append Monday Data to main
    Main.append('1')
    for key,val in monday_1.items():
        S1 = val
        Main.append(S1)
    
    monday_2 = Master('Monday', '2')
    Main.append('2')
    for key,val in monday_2.items():
        S1 = val
        Main.append(S1)
    
    monday_3 = Master('Monday', '3')
    Main.append('3')
    for key,val in monday_3.items():
        S1 = val
        Main.append(S1)
    
    monday_4 = Master('Monday', '4')
    Main.append('4')
    for key,val in monday_4.items():
        S1 = val
        Main.append(S1)
    
    monday_5 = Master('Monday', '5')
    Main.append('5')
    for key,val in monday_5.items():
        S1 = val
        Main.append(S1)
    
    monday_6 = Master('Monday', '6')
    Main.append('6')
    for key,val in monday_6.items():
        S1 = val
        Main.append(S1)
    
    monday_7 = Master('Monday', '7')
    Main.append('7')
    for key,val in monday_7.items():
        S1 = val
        Main.append(S1)
    
    monday_8 = Master('Monday', '8')
    Main.append('8')
    for key,val in monday_8.items():
        S1 = val
        Main.append(S1)

    #Append Tuesday Data to main
    tuesday_1 = Master('Tuesday', '1')
    Main.append('1')
    for key,val in tuesday_1.items():
        S1 = val
        Main.append(S1)
    
    tuesday_2 = Master('Tuesday', '2')
    Main.append('2')
    for key,val in tuesday_2.items():
        S1 = val
        Main.append(S1)
    
    tuesday_3 = Master('Tuesday', '3')
    Main.append('3')
    for key,val in tuesday_3.items():
        S1 = val
        Main.append(S1)
    
    tuesday_4 = Master('Tuesday', '4')
    Main.append('4')
    for key,val in tuesday_4.items():
        S1 = val
        Main.append(S1)
    
    tuesday_5 = Master('Tuesday', '5')
    Main.append('5')
    for key,val in tuesday_5.items():
        S1 = val
        Main.append(S1)
    
    tuesday_6 = Master('Tuesday', '6')
    Main.append('6')
    for key,val in tuesday_6.items():
        S1 = val
        Main.append(S1)
    
    tuesday_7 = Master('Tuesday', '7')
    Main.append('7')
    for key,val in tuesday_7.items():
        S1 = val
        Main.append(S1)
    
    tuesday_8 = Master('Tuesday', '8')
    Main.append('8')
    for key,val in tuesday_8.items():
        S1 = val
        Main.append(S1)
    
    #append Wednesday Values to Main
    wednesday_1 = Master('Wednesday', '1')
    Main.append('1')
    for key,val in wednesday_1.items():
        S1 = val
        Main.append(S1)
    
    wednesday_2 = Master('Wednesday', '2')
    Main.append('2')
    for key,val in wednesday_2.items():
        S1 = val
        Main.append(S1)

    wednesday_3 = Master('Wednesday', '3')
    Main.append('3')
    for key,val in wednesday_3.items():
        S1 = val
        Main.append(S1)
    
    wednesday_4 = Master('Wednesday', '4')
    Main.append('4')
    for key,val in wednesday_4.items():
        S1 = val
        Main.append(S1)
    Main.append('5')

    wednesday_5 = Master('Wednesday', '5')
    for key,val in wednesday_5.items():
        S1 = val
        Main.append(S1)
    
    wednesday_6 = Master('Wednesday', '6')
    Main.append('6')
    for key,val in wednesday_6.items():
        S1 = val
        Main.append(S1)
    
    wednesday_7 = Master('Wednesday', '7')
    Main.append('7')
    for key,val in wednesday_7.items():
        S1 = val
        Main.append(S1)
    
    wednesday_8 = Master('Wednesday', '8')
    Main.append('8')
    for key,val in wednesday_8.items():
        S1 = val
        Main.append(S1)

    #append Thursday Values to Main
    thursday_1 = Master('Thursday', '1')
    Main.append('1')
    for key,val in thursday_1.items():
        S1 = val
        Main.append(S1)

    thursday_2 = Master('Thursday', '2')
    Main.append('2')
    for key,val in thursday_2.items():
        S1 = val
        Main.append(S1)
    
    thursday_3 = Master('Thursday', '3')
    Main.append('3')
    for key,val in thursday_3.items():
        S1 = val
        Main.append(S1)
    
    thursday_4 = Master('Thursday', '4')
    Main.append('4')
    for key,val in thursday_4.items():
        S1 = val
        Main.append(S1)
    
    thursday_5 = Master('Thursday', '5')
    Main.append('5')
    for key,val in thursday_5.items():
        S1 = val
        Main.append(S1)
    
    thursday_6 = Master('Thursday', '6')
    Main.append('6')
    for key,val in thursday_6.items():
        S1 = val
        Main.append(S1)
    
    thursday_7 = Master('Thursday', '7')
    Main.append('7')
    for key,val in thursday_7.items():
        S1 = val
        Main.append(S1)
    
    thursday_8 = Master('Thursday', '8')
    Main.append('8')
    for key,val in thursday_8.items():
        S1 = val
        Main.append(S1)

    #append Friday Values to Main
    friday_1 = Master('Friday', '1')
    Main.append('1')
    for key,val in friday_1.items():
        S1 = val
        Main.append(S1)
    
    friday_2 = Master('Friday', '2')
    Main.append('2')
    for key,val in friday_2.items():
        S1 = val
        Main.append(S1)
    
    friday_3 = Master('Friday', '3')
    Main.append('3')
    for key,val in friday_3.items():
        S1 = val
        Main.append(S1)
    
    friday_4 = Master('Friday', '4')
    Main.append('4')
    for key,val in friday_4.items():
        S1 = val
        Main.append(S1)
    
    friday_5 = Master('Friday', '5')
    Main.append('5')
    for key,val in friday_5.items():
        S1 = val
        Main.append(S1)
    
    friday_6 = Master('Friday', '6')
    Main.append('6')
    for key,val in friday_6.items():
        S1 = val
        Main.append(S1)
    
    friday_7 = Master('Friday', '7')
    Main.append('7')
    for key,val in friday_7.items():
        S1 = val
        Main.append(S1)
    
    friday_8 = Master('Friday', '8')
    Main.append('8')
    for key,val in friday_8.items():
        S1 = val
        Main.append(S1)


    #append Saturday Values to Main
    saturday_1 = Master('Saturday', '1')
    Main.append('1')
    for key,val in saturday_1.items():
        S1 = val
        Main.append(S1)
    
    saturday_2 = Master('Saturday', '2')
    Main.append('2')
    for key,val in saturday_2.items():
        S1 = val
        Main.append(S1)
    
    saturday_3 = Master('Saturday', '3')
    Main.append('3')
    for key,val in saturday_3.items():
        S1 = val
        Main.append(S1)

    saturday_4 = Master('Saturday', '4')
    Main.append('4')
    for key,val in saturday_4.items():
        S1 = val
        Main.append(S1)
    
    saturday_5 = Master('Saturday', '5')
    Main.append('5')
    for key,val in saturday_5.items():
        S1 = val
        Main.append(S1)
    
    saturday_6 = Master('Saturday', '6')
    Main.append('6')
    for key,val in saturday_6.items():
        S1 = val
        Main.append(S1)

    print ('Len of main Function : ',len(Main))
    #print (Main)
    return Main