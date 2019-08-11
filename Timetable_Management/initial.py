from flask import Flask, render_template, request, send_from_directory, redirect, url_for,session,g,flash
from sqlalchemy import create_engine,text
import pymysql

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def initial_setup():
    if request.method == 'POST':
        db_name = request.form.get('Db_Name')
        db = create_engine('mysql+pymysql://root1:password@localhost')
        connection = db.connect()
        connection.execute("create database "+db_name)
        return 'Database Created'
    else:
        return render_template('initial_setup.html')

if __name__ == "__main__":
    app.run('0.0.0.0',debug=True, port=5001)