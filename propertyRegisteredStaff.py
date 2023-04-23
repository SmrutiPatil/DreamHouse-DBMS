import mysql.connector
import os
from dotenv import load_dotenv 
import tkinter as tk

load_dotenv()

mysqldb = mysql.connector.connect(host="localhost", user=os.getenv("db_user"), password=os.getenv("db_password"), database=os.getenv("db_name"))
mycursor = mysqldb.cursor()

def propertyList(id, staff_dash_window):
    staff_num = id
    sql = ("select property_number, owner_num, is_rented from property where managed_by = %s;")
    mycursor.execute(sql, [staff_num])
    prop_details = mycursor.fetchall()

    staff_f1= tk.Frame(staff_dash_window)
    staff_f1.grid(row=2, column=0, padx=10)

    for label in staff_f1.grid_slaves():
        if int(label.grid_info()["row"]) > 0:
            label.grid_forget()

    # Staff Numbers
    prop_num_label = tk.Label(staff_f1, text="Property Number", font=("Helvetica", 10, "bold"))
    prop_num_label.grid(column=0, row=0, padx=50)

    # Name
    own_num_label = tk.Label(staff_f1, text="Owner Number", font=("Helvetica", 10,"bold"))
    own_num_label.grid(column=1, row=0, padx=50)

    # Position
    pos_num_label = tk.Label(staff_f1, text="Rented?(Y/N)", font=("Helvetica", 10,"bold"))
    pos_num_label.grid(column=2, row=0, padx=50)

    for i in range(len(prop_details)):

        prop_num_label = tk.Label(staff_f1, text=prop_details[i][0], font=("Helvetica", 10))
        prop_num_label.grid(column=0, row=i+1, padx=50)

        # Name
        owner_num_label = tk.Label(staff_f1, text=prop_details[i][1], font=("Helvetica", 10))
        owner_num_label.grid(column=1, row=i+1, padx=50)

        # Position
        isRented_label = tk.Label(staff_f1, text=prop_details[i][2], font=("Helvetica", 10))
        isRented_label.grid(column=2, row=i+1, padx=50)

    # for prop in prop_details:
    #     print(prop)
