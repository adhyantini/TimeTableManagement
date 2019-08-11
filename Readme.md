# Time Table Management System - WebApp
The timetable management system aims at simplifying the professors work by sorting the master time table(time table containing all classes in a department's schedule) into different timetables according to need. For example: The professor can view the schedule of a particular classroom for an entire week, or the weekly schedule of any professor, or weekly schedule of a particular batch such as FE,TE,BE, etc.The system also has options for helping the teacher create and edit a timetable. 

## Features
The application is well equipped with a secure login system where the user's data is cryptographically secure.The dashboard of the application provides the navigation to various pages like edit timetable , view timetable, create timetable,etc. Each page has a navbar for easy navigation within the application. 

## Techical Overview 
Backend Technologies
* Python Flask
* Python - Bcrypt (For Login Management)

Front End Technologies
* Jinja 2
* HTML
* CSS
* Bootstrap
* JS
* Jquery

Database
* SQL

## Dependencies
* It is compatible with Python 2.6, 2.7 and 3.3+.
* It needs SQl installed on the system.
## Security
Login Management of the system would prevent the application from basic SQL Injections. User password and other sensitive data is securely stored.

## System Setup
#### Create a Python Virtual Env <br>
<code>pip3 -r install requirements.txt</code><br>
<code>SQL - Create a db with name *TimeTable*</code><br>
<code>python3 create_table.py</code><br>
#### Add a user to the login table in the db using the INSERT command. Finally run

<code>python3 app.py</code>
