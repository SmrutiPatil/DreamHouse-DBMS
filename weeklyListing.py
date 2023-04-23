import mysql.connector
import os
from dotenv import load_dotenv 
import tkinter as tk
from tkinter import ttk
from tkcalendar import *

load_dotenv()

mysqldb = mysql.connector.connect(host="localhost", user=os.getenv("db_user"), password=os.getenv("db_password"), database=os.getenv("db_name"))
mycursor = mysqldb.cursor()

def weekly_listing(id, client_dash_board):
    sql1=("select property_number, type, CONCAT(PStreet, ', ', PCity, ', ', PPincode) AS address from property where Registered_At_Branch = (select Branch_Number from client where Client_Number=%s)")
    mycursor.execute()

    sql2=("select Branch_Number, CONCAT(BStreet, ', ', BCity, ', ', BPincode), BPhone_Number from branch where branch_number = (select Branch_Number from client where Client_Number=%s );")

    