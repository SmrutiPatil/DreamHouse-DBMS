import mysql.connector
import os
import tkinter as tk
from dotenv import load_dotenv
from com_function import warningWindow, connect



mydb = connect()

dbCursor = mydb.cursor()
def radio_button_clicked():
  is_business = var.get()

def ownerDashboard(self):
  Personal_or_Business_name= owner_name_entry.get()
  Owner_Number=  owner_number_entry.get()
  OAddress= owner_addr_entry.get()
  OCity=owner_city_entry.get()
  OPincode=owner_picode_entry.get()
  Telephone_Number= owner_tel_entry.get()
  if(Personal_or_Business_name=="" or   Owner_Number=="" or  OAddress=="" or  OCity=="" or  OPincode=="" or Telephone_Number==""):
       warningWindow("Need Valid Input for all fields")

  else:
    con=mysql.connect(host="localhost", user="",password="",database="")
    cursor=con.cursor()
    cursor.execute("insert into owner values('"+ Personal_or_Business_name + "','" + is_business + "','" + Owner_Number + "','" +  OAddress + "','" +  OCity + "','" +   OPincode + "','" +   Telephone_Number + "')")
    cursor.execute("commit")
    warningWindow("Inserted Successfully")