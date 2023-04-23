import mysql.connector
import os
from dotenv import load_dotenv
import tkinter as tk

load_dotenv()

mydb = mysql.connector.connect( host= "localhost",
                               user= os.getenv("DB_USER"),
                               password= os.getenv("DB_PASSWORD"),
                               database = os.getenv("DB_NAME"))

dbCursor = mydb.cursor()

import com_function as cf


def validateUser(role, id):
    db = cf.connect()
    dbCursor = db.cursor()
    dbCursor.execute(f"""SELECT * FROM {role} WHERE {role}_number = '{id}'""")
    user = dbCursor.fetchone()
    if user:
        return True
    else:
        cf.warningWindow("Login failed")
        return False
    
#def registerStaff(id):
    
