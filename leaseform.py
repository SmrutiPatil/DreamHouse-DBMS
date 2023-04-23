import mysql.connector
import os
from dotenv import load_dotenv 
import tkinter as tk

load_dotenv()

mysqldb = mysql.connector.connect(host="localhost", user=os.getenv("db_user"), password=os.getenv("db_password"), database=os.getenv("db_name"))
mycursor = mysqldb.cursor()

lease_window = tk.Tk()