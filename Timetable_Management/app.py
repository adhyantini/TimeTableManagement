from flask import Flask, render_template, request, send_from_directory, redirect, url_for,session,g,flash,send_file
from flask_bcrypt import Bcrypt
import flask_excel
import pyexcel
import db_connect
from db_connect import *
import sqlalchemy
from sqlalchemy import create_engine,text
from werkzeug.utils import secure_filename
import xlrd
import create_excel
from create_excel import *
import view_teacher
from view_teacher import *
import view_location
from view_location import *
import view_batch
from view_batch import *
import view_master
from view_master import *
from jinja2 import Template
# Open the workbook and define the worksheet


ALLOWED_EXTENSIONS = set(['xls'])
app = Flask(__name__)
app.secret_key = 'shhhh'
flask_excel.init_excel(app)
bcrypt = Bcrypt(app)
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods =['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = db_connect()
        connection = db.connect()
        username = request.form.get('username')
        password = request.form.get('password')
        password_hash = bcrypt.generate_password_hash(password)
        #bcrypt.check_password_hash(password_hash, password)
        print (password_hash)
        sql_user = "SELECT Username, Password FROM login WHERE  Username ='"+username+"'"
        user_result = connection.execute(sql_user)
        user_res = user_result.fetchall()
        user_res_str = str(user_res)
        print (user_res)
        print (user_result)


        #-- Check if Public-Key is Present
        if len(user_res_str) != 2:
            for row in user_res:
                pas = row['Password']
                us = row['Username']
                val = bcrypt.check_password_hash(password_hash, pas)
                if username == us and val == True:
                    session['user'] = username
                    print ('Authentication Successfull!')
                    return redirect(url_for('dashboard'))
                else:
                    return 'Incorrect Login Credentials'           
  
        else:
            return 'Incorrect Login Credentials'
    else:
        return render_template('login.html')




@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if g.user:
        if request.method == 'POST':
            return redirect(url_for('view_timetable'))
            return 'Dashboard Tried Posting'
        else:
            return render_template('Dashboard.html')

    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'GET':
        session.clear()
        return redirect(url_for('login'))


@app.route('/view_timetable', methods=['GET', 'POST'])
def view_timetable():
    if g.user:
        if request.method == 'POST':
            return 'view_tt Tried Posting'
        else:
            return render_template('View_TT.html')
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if g.user:
        if request.method == 'POST':
            
            db = db_connect()
            connection = db.connect()
            
            
            if request.form.get('button_change_username') ==  'button_change_username':
                
                email = request.form.get("email_address1")
                username = request.form.get("new_username1")
                username_confirm = request.form.get("new_username_confirm1")
                password = request.form.get("password1")
                
                sql_user = "SELECT Email,Password FROM login WHERE  Email ='"+email+"' and Password = '"+password+"'"
                user_result = connection.execute(sql_user)
                user_res = user_result.fetchall()
                user_res_str = str(user_res)
                print (user_res)
                print (user_result)
                if len(user_res_str) != 2:
                    
                    print ('Data Present!')
                    sql_pass = "UPDATE login set Username = '"+username_confirm+"' WHERE  Email ='"+email+"' and Password ='"+password+"' "
                    user_result1 = connection.execute(sql_pass)
                    print("Updated Successfully")
                    print(sql_pass)
                    data = ' Username Updated successfully.'
                    
                    return render_template('Settings.html',data = data)                
                
                else:
                    
                    data = 'Incorrect Credentials'
                    
                    return render_template('Settings.html',data = data)
            
            
            elif request.form.get('button_change_password') == 'button_change_password' :
                
                email = request.form.get("email_address2")
                username = request.form.get("username2")
                password = request.form.get("new_password2")
                password_confirm = request.form.get("conf_password2")
                print (email,username,password,password_confirm)
                
                if(password != password_confirm):
                    
                    data2 = 'Password and Confirm Password do not match'
                    
                    return render_template('Settings.html', data2 = data2)
                
                else:
                    
                    sql_user = "SELECT Email,Username FROM login WHERE  Email ='"+email+"' and Username ='"+username+"'"
                    user_result = connection.execute(sql_user)
                    user_res = user_result.fetchall()
                    user_res_str = str(user_res)
                    print (user_res)
                    print (user_result)
                    
                    if len(user_res_str) != 2:
                        
                        print ('Data Present!')
                        sql_pass = "UPDATE login set Password = '"+password_confirm+"' WHERE  Email ='"+email+"' and Username ='"+username+"'"
                        user_result1 = connection.execute(sql_pass)
                        print("Updated Successfully")
                        print(sql_pass)
                        data3 = ' Password Updated successfully.'
                        
                        return render_template('Settings.html',data2 = data3)                
                    
                    else:
                        
                        return 'Incorrect Credentials' 

            
            elif request.form.get('button_add_user') == 'button_add_user':
                
                email = request.form.get("email_address3")
                username = request.form.get("add_username3")
                password = request.form.get("add_password3")
                password_confirm = request.form.get("confirm_add_password3")
                #password_hash = bcrypt.generate_password_hash(password_confirm)
                if(password != password_confirm):
                    
                    data4 = 'Password and Confirm Password do not match'
                    
                    return render_template('Settings.html', data3 = data4)
                
                else:
                    
                    sql_pass = "INSERT into login(Username,Email,Password) values ('"+ username+ "' , '"+email+"', '"+password+"') "
                    user_result1 = connection.execute(sql_pass)
                    print("Updated Successfully")
                    print(sql_pass)
                    data5 = ' New User Added Successfully.'
                    
                    return render_template('Settings.html',data3 = data5)               
            
                    
        else:
            
            return render_template('Settings.html')
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        db = db_connect()
        connection = db.connect()
        email = request.form.get('email')
        username = request.form.get('username')
        new_password = request.form.get('password')
        sql_user = "SELECT Email,Username FROM login WHERE  Email ='"+email+"' and Username ='"+username+"'"
        user_result = connection.execute(sql_user)
        user_res = user_result.fetchall()
        user_res_str = str(user_res)
        print (user_res)
        print (user_result)


        #-- Check if Public-Key is Present
        if len(user_res_str) != 2:
            print ('Data Present!')
            sql_pass = "UPDATE login set Password = '"+new_password+"' WHERE  Email ='"+email+"' and Username ='"+username+"' "
            user_result1 = connection.execute(sql_pass)
            print("Updated Successfully")
            print(sql_pass)
            data = ' Password Updated successfully.'
            return redirect(url_for('login'))                
        else:
            data = 'Incorrect Credentials'        
    else:
        return render_template('Forgot_Password.html')


@app.route('/create_timetable', methods=['GET', 'POST'])
def create_tt():
    if g.user:
        if request.method == 'POST':
            
            db = db_connect()
            connection = db.connect()
            Day = request.form.get('Day')
            Slot = request.form.get('Slot')
            Location = request.form.get('Location')
            Division = request.form.get('Division')
            Batch = request.form.get('Batch')
            Subject = request.form.get('Subject')
            Faculty = request.form.get('Faculty')
            Sem = request.form.get('Sem')
            print (Day,Slot,Location,Division,Batch,Subject,Faculty,Sem)
            data = check_validation(Sem)

            if Sem == 'Sem1': 
                if data == True:
                    url_sem1 = "Insert into master_sem1 (Day, Slot, Location, Batch, Subject, Faculty) values ('"+Day+"' , '"+Slot+"' , '"+Location+"' , '"+Batch+"' , '"+Subject+"' , '"+Faculty+"' )"
                    print (url_sem1)
                    connection.execute (url_sem1)
                    message = 'Data Updated Successfully'
                    return render_template ('Success_data.html' , data = message)
                else:
                    message = 'Cannot Insert Data As Database Slots Are Full'
                    return render_template('Success_data.html', data = message)
            
            else:
                if data == True:
                    url_sem2 = "Insert into master_sem2 (Day, Slot, Location, Batch, Subject, Faculty) values ('"+Day+"' , '"+Slot+"' , '"+Location+"' , '"+Batch+"' , '"+Subject+"' , '"+Faculty+"' )"
                    connection.execute (url_sem2)
                    message = 'Data Updated Successfully'
                    return render_template ('Success_data.html' , data = message)
                else:
                    message = 'Cannot Insert Data As Database Slots Are Full'
                    return render_template('Success_data.html', data = message)
        else:
            
            return render_template('Enter_Data_Form.html')
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''


def check_validation(Sem):
    
    db = db_connect()
    connection = db.connect()
    if Sem == 'Sem1':
        monday = connection.execute("select count(*) from master_sem1 where day = 'Monday'")
        monday_res = monday.fetchall()
        for row in monday_res:
            count_monday = row['count(*)']

        tuesday = connection.execute("select count(*) from master_sem1 where day = 'Tuesday'")
        tuesday_res = tuesday.fetchall()
        for row in tuesday_res:
            count_tuesday = row['count(*)']
        
        wednesday = connection.execute("select count(*) from master_sem1 where day = 'Wednesday'")
        wednesday_res = wednesday.fetchall()
        for row in wednesday_res:
            count_wednesday = row['count(*)']
        
        thursday = connection.execute("select count(*) from master_sem1 where day = 'Thursday'")
        thursday_res = thursday.fetchall()
        for row in thursday_res:
            count_thursday = row['count(*)']
        
        friday = connection.execute("select count(*) from master_sem1 where day = 'Friday'")
        friday_res = friday.fetchall()
        for row in friday_res:
            count_friday = row['count(*)']

        saturday = connection.execute("select count(*) from master_sem1 where day = 'Saturday'")
        saturday_res = saturday.fetchall()
        for row in saturday_res:
            count_saturday = row['count(*)']
        print (type(count_monday),count_tuesday,count_wednesday,count_thursday,count_friday,count_saturday)
        if count_monday == 120 or count_tuesday == 120 or count_wednesday == 120 or count_thursday == 120 or count_friday == 120 or count_saturday == 90:
            return False
        
        else:
            return True
    
    elif Sem == 'Sem2':
        
        monday = connection.execute("select count(*) from master_sem2 where day = 'Monday'")
        monday_res = monday.fetchall()
        for row in monday_res:
            count_monday = row['count(*)']

        tuesday = connection.execute("select count(*) from master_sem2 where day = 'Tuesday'")
        tuesday_res = tuesday.fetchall()
        for row in tuesday_res:
            count_tuesday = row['count(*)']
        
        wednesday = connection.execute("select count(*) from master_sem2 where day = 'Wednesday'")
        wednesday_res = wednesday.fetchall()
        for row in wednesday_res:
            count_wednesday = row['count(*)']
        
        thursday = connection.execute("select count(*) from master_sem2 where day = 'Thursday'")
        thursday_res = thursday.fetchall()
        for row in thursday_res:
            count_thursday = row['count(*)']
        
        friday = connection.execute("select count(*) from master_sem2 where day = 'Friday'")
        friday_res = friday.fetchall()
        for row in friday_res:
            count_friday = row['count(*)']

        saturday = connection.execute("select count(*) from master_sem2 where day = 'Saturday'")
        saturday_res = saturday.fetchall()
        for row in saturday_res:
            count_saturday = row['count(*)']

        if count_monday == 120 or count_tuesday == 120 or count_wednesday == 120 or count_thursday == 120 or count_friday == 120 or count_saturday == 90:
            return False
        
        else:
            return True


@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if g.user:
        if request.method == 'POST':
            array = request.get_array(field_name='file')
            print(array [0])
            print('hey bro')
            for i in array[0]:
                print(i)
            
            #fil = request.files('file')
            #book = xlrd.open_workbook(fil)
            #sheet = book.sheet_by_name("Sheet1")
            #print (book)
            return jsonify({"result": array})
            
        return '''
        <!doctype html>
        <title>Upload an excel file</title>
        <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
        <form action="" method=post enctype=multipart/form-data>
        <p><input type=file name=file><input type=submit value=Upload>
    </form>
        '''
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''


@app.route('/view_timetable_master', methods=['GET', 'POST'])
def view_tt_master():
    if g.user:
        if request.method == 'POST':
            if request.form.get('submit') ==  'submit':
                data = view_master()
                print (data)
                return render_template('Master_TT.html' , data = data )
            elif request.form.get('download') ==  'download':
                data = view_master()
                print (data)
                test_loc = excel_master(data)
                path = test_loc
                return send_file(path, as_attachment=True)
                
        else:
            data = ''
            return render_template('Master_TT.html' , data = data )
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''


@app.route('/view_timetable_teacher', methods=['GET', 'POST'])
def view_tt_teacher():
    if g.user:
        if request.method == 'POST':
            teacher = request.form.get('teacher_name')
            if request.form.get('submit') ==  'submit':
                data = view_teacher(teacher)
                print (data)
                return render_template('Teacher_TT.html' , data = data)
            elif request.form.get('download') ==  'download':     
                data = view_teacher(teacher)
                print (data)
                test_loc = excel_teacher(data)
                path = test_loc
                return send_file(path, as_attachment=True)
        else:
            data = ''
            return render_template('Teacher_TT.html', data = data)
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''


@app.route('/view_timetable_location', methods=['GET', 'POST'])
def view_tt_location():
    if g.user:
        if request.method == 'POST':
            location = request.form.get('Edit_Faculty_Location')
            if request.form.get('submit') ==  'submit':
                data = view_location(location)
                print (location)
                return render_template('Location_TT.html', data = data)
            elif request.form.get('download') ==  'download':
                data = view_location(location)
                print (location)
                test_loc = excel_location(data)
                path = test_loc
                return send_file(path, as_attachment=True)    

        else:
            data = ''
            return render_template('Location_TT.html', data = data)
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''

@app.route('/view_timetable_batch', methods=['GET', 'POST'])
def view_tt_batch():
    if g.user:
        if request.method == 'POST':
            shift = request.form.get('Edit_Shift_TT')
            batch = request.form.get('Edit_Batch_TT')
            if request.form.get('submit') ==  'submit':
                print(batch)
                print(shift)
                data = fetch_batch(batch,shift)
                print ('NewFunction Fetch batch executed sucessfully')
                print (data)
                return render_template('Batch_TT.html', data = data )
            elif request.form.get('download') ==  'download':
                data = fetch_batch(batch,shift)
                test_loc = excel_batch(batch,shift,data) 
                path = test_loc
                return send_file(path, as_attachment=True)    

            
        else:
            data = ''
            return render_template('Batch_TT.html', data = data)
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''

def fetch_batch(batch,shift):
    if batch == 'FE' and shift == '1':
        grade = '^F1'
        data = view_batch(grade)
    elif batch == 'FE' and shift == '2':
        grade = '^F2'
        data = view_batch(grade)
    elif batch == 'SE' and shift == '1':
        grade = '^S1'
        data = view_batch(grade)
    elif batch == 'SE' and shift == '2':
        grade = '^S2'
        data = view_batch(grade)
    elif batch == 'TE' and shift == '1':
        grade = '^T1'
        data = view_batch(grade)
    elif batch == 'TE' and shift == '2':
        grade = '^T2'
        data = view_batch(grade)
    elif batch == 'BE' and shift == '1':
        grade = '^B1'
        data = view_batch(grade)
    elif batch == 'BE' and shift == '2':
        grade = '^B2'
        data = view_batch(grade)
    elif batch == 'ME' and shift == '1':
        grade = '^M1'
        data = view_batch(grade)
    elif batch == 'ME' and shift == '2':
        grade = '^M2'
        data = view_batch(grade)
    return data


@app.route("/export", methods=['GET'])
def export_records():
    if g.user:
        
        path = "./excel/FE1.xlsx"
        return send_file(path, as_attachment=True)    
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''


@app.route('/edit_timetable', methods=['GET', 'POST'])
def edit_timetable():
    if g.user:
        if request.method == 'POST':
            return redirect(url_for('dashboard'))
        else:
            return render_template('Edit.html')
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''

@app.route('/edit_timetable_faculty', methods=['GET', 'POST'])
def edit_timetable_faculty():
    if g.user:
        if request.method == 'POST':
            db = db_connect()
            connection = db.connect()
            
            Day = request.form.get('Edit_Faculty_Day')
            Slot = request.form.get('Edit_Faculty_Slot')
            Location = request.form.get('Edit_Faculty_Location')
            Faculty = request.form.get('teacher_name')
            Semester_Number = request.form.get('Semester_Number')
            
            #print (Day,Slot,Location)
            sql = "select Faculty from master_sem"+Semester_Number+ " where Day = '"+Day+"' and Slot= '"+Slot+"' and Location = '"+Location+"'"
            result = connection.execute(sql)
            res = result.fetchall()
            str_res = str(res)
            if len(str_res) != 2:
                
                print ('Data Found. Will update.' )
                sql1 = "update master_sem"+Semester_Number+ " set Faculty = '"+Faculty+"' where Day = '"+Day+"' and Slot='" +Slot+"' and Location = '"+Location+"'"
                print (sql1)
                connection.execute(sql1)
                print('Update successful')
                message2 = 'Update successful'
                return render_template('Edit_Faculty.html', data=message2)    
            
            else:
                
                print('Data Not found. Please enter correct cell to update')    
                message3 = 'Data Not found. Please enter correct cell to update'    
                return render_template('Edit_Faculty.html',data = message3)
        
        else:
            
            return render_template('Edit_Faculty.html')
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''
        
@app.route('/edit_timetable_subject', methods=['GET', 'POST'])
def edit_timetable_subject():
    if g.user:
        if request.method == 'POST':
            db = db_connect()
            connection = db.connect()
            Day = request.form.get('Edit_Subject_Day')
            Slot = request.form.get('Edit_Subject_Slot')
            Location = request.form.get('Edit_Subject_Location')
            Subject = request.form.get('subject_name')
            Semester_Number = request.form.get('Semester_Number')
            print (Day,Slot,Location)
            sql = "select Subject from master_sem"+Semester_Number+ " where Day = '"+Day+"' and Slot= '"+Slot+"' and Location = '"+Location+"'"
            result = connection.execute(sql)
            res = result.fetchall()
            str_res = str(res)
            if len(str_res) != 2:
                print ('Data Found. Will update.' )
                sql1 = "update master_sem"+Semester_Number+ " set Subject = '"+Subject+"' where Day = '"+Day+"' and Slot='" +Slot+"' and Location = '"+Location+"'"
                print (sql1)
                connection.execute(sql1)
                print('Update successful')
                message2 = 'Update successful'
                return render_template('Edit_Subject.html', data=message2)    
            else:
                print('Data Not found. Please enter correct cell to update')    
                message3 = 'Data Not found. Please enter correct cell to update'    
                return render_template('Edit_Subject.html',data = message3)
        else:
            
            return render_template('Edit_Subject.html')
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''

@app.route('/edit_timetable_batch', methods=['GET', 'POST'])
def edit_timetable_location():
    if g.user:
        if request.method == 'POST':
            db = db_connect()
            connection = db.connect()
            Day = request.form.get('Edit_Batch_Day')
            Slot = request.form.get('Edit_Batch_Slot')
            Location = request.form.get('Edit_Batch_Location')
            Batch = request.form.get('batch_name')
            Semester_Number = request.form.get('Semester_Number')
            print (Day,Slot,Location)
            sql = "select Batch from master_sem"+Semester_Number+ " where Day = '"+Day+"' and Slot= '"+Slot+"' and Location = '"+Location+"'"
            result = connection.execute(sql)
            res = result.fetchall()
            str_res = str(res)
            if len(str_res) != 2:
                print ('Data Found. Will update.' )
                sql1 = "update master_sem"+Semester_Number+ " set Batch = '"+Batch+"' where Day = '"+Day+"' and Slot='" +Slot+"' and Location = '"+Location+"'"
                print (sql1)
                connection.execute(sql1)
                print('Update successful')
                message2 = 'Update successful'
                return render_template('Edit_Class.html', data=message2)    
            else:
                print('Data Not found. Please enter correct cell to update')    
                message3 = 'Data Not found. Please enter correct cell to update'    
                return render_template('Edit_Class.html',data = message3)
        else:
            
            return render_template('Edit_Class.html')
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''



@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if g.user:
        if request.method == 'POST':
            db = db_connect()
            connection = db.connect()
            sql1 = 'Delete from master_sem1'
            connection.execute(sql1)
            sql2 = 'Delete from master_sem2'
            connection.execute(sql2)
            print ('All Data Cleared')
            return redirect(url_for('dashboard'))
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''


@app.route('/create_table', methods=['GET', 'POST'])
def create_table():
    if g.user:
        if request.method == 'POST':
            db = db_connect()
            connection = db.connect()
            print ('DATABASE CONNECTED....PERFORMING OTHER OPERATIONS')
            connection.execute('create table master_sem1 (Id INT NOT NULL AUTO_INCREMENT,Day varchar(30), Slot varchar(30), Location varchar(30), Batch varchar(30), Subject varchar(30), Faculty varchar(100), PRIMARY KEY (Id) )')
            connection.execute('create table master_sem2 (Id int NOT NULL AUTO_INCREMENT,Day varchar(30), Slot varchar(30), Location varchar(30), Batch varchar(30), Subject varchar(30), Faculty varchar(100), PRIMARY KEY (Id) )')
            connection.execute('create table login (Username varchar(50), Email varchar(50), Password varchar(50))')
            connection.execute('create table teacher_data (Name varchar(100), Initials varchar(10))')
            return redirect(url_for('dashboard'))

    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''




@app.route('/edit_timetable_all', methods=['GET', 'POST'])
def edit_timetable_all():
    if g.user:
        if request.method == 'POST':
            db = db_connect()
            connection = db.connect()
            Day = request.form.get('Edit_All_Day')
            Slot = request.form.get('Edit_All_Slot')
            Location = request.form.get('Edit_All_Location')
            Batch = request.form.get('Batch_name_all')
            Subject = request.form.get('Subject_name_all')
            Faculty = request.form.get('Teacher_name_all')
            Semester_Number = request.form.get('Semester_Number')
            print (Day,Slot,Location)
            sql = "select Batch,Faculty,Subject from master_sem"+Semester_Number+ " where Day = '"+Day+"' and Slot= '"+Slot+"' and Location = '"+Location+"'"
            result = connection.execute(sql)
            res = result.fetchall()
            str_res = str(res)
            if len(str_res) != 2:
                print ('Data Found. Will update.' )
                sql1 = "update master_sem"+Semester_Number+ " set Batch = '"+Batch+"' , Subject = '"+Subject+ "' , Faculty = '"+Faculty+"' where Day = '"+Day+"' and Slot='" +Slot+"' and Location = '"+Location+"'"
                print (sql1)
                connection.execute(sql1)
                print('Update successful')
                message2 = 'Update successful'
                return render_template('Edit_All.html', data=message2)    
            else:
                print('Data Not found. Please enter correct cell to update')    
                message3 = 'Data Not found. Please enter correct cell to update'    
                return render_template('Edit_All.html',data = message3)
        else:
            
            return render_template('Edit_All.html')
    return '''<h2>Unauthorised Access Visit <a href ='/login'>login<a></h2>'''

@app.before_request

#-- Checks For Active Sessions

def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

if __name__ == "__main__":
    app.run('0.0.0.0',debug=True, port=5000)



'''book = xlrd.open_workbook("atpstm.xls")
sheet = book.sheet_byJ

# Establish a MySQL connection
# Create the INSERT INTO sql query
query = """INSERT INTO master (Day , Slot , Location, Batch, Subject, Faculty) VALUES (%s, %s, %s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
    Day		= sheet.cell(r,0).value
    Time	= sheet.cell(r,1).value
    Location		= sheet.cell(r,2).value
    Batch		= sheet.cell(r,3).value
    Subject	= sheet.cell(r,4).value
    Faculty	    = sheet.cell(r,5).value
    
	# Assign values from each row
    #values = (Day , Time , SL1 , SL2 , SysL , HL , PR , PL , ONL1 , ONL2 , ONL3 , PGL , R422 , R424 , R320 , R325 , R420B )

	# Execute sql Query
    connection.execute(query, values)

columns = str(sheet.ncols)
rows = str(sheet.nrows)
#print ("I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!")
print ('DONE')
'''
