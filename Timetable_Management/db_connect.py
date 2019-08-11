import sqlalchemy
from sqlalchemy import create_engine,text
import pymysql
#-- Connect To Db
def db_connect():
    engine = create_engine('mysql+pymysql://root1:password@localhost/TimeTable')
    # Create a Cursor object to execute queries.
    print ('Connected To Database')
    return engine