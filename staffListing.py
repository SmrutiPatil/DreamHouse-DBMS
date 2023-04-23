import mysql.connector
import os
from dotenv import load_dotenv 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from subprocess import call

load_dotenv()

mysqldb = mysql.connector.connect(host="localhost", user=os.getenv("db_user"), password=os.getenv("db_password"), database=os.getenv("db_name"))
mycursor = mysqldb.cursor()

def staffListing(branch_num, staff_f1, staff_f2):
    branch_num=branch_num.get()
    sql1 = ("SELECT staff_number, staff_name, position FROM staff where branch_number= %s")
    mycursor.execute(sql1, [branch_num])
    staff_details = mycursor.fetchall()

    sql2 = ("SELECT CONCAT(BStreet, ', ', BCity, ', ', BPincode) AS address, BPhone_Number FROM Branch WHERE Branch_Number = %s;")
    mycursor.execute(sql2, [branch_num])
    branch_details = mycursor.fetchall()

    for label in staff_f1.grid_slaves():
        if int(label.grid_info()["row"]) > 0:
            label.grid_forget()

    for label in staff_f2.grid_slaves():
        if int(label.grid_info()["row"]) > 0:
            label.grid_forget()

    # branch address
    branch_addr_label = tk.Label(staff_f1, text="Branch Address:", font=("Helvetica", 10))
    branch_addr_label.grid(column=2, row=0, padx=10)
    branch_addr_label = tk.Label(staff_f1, text=branch_details[0][0], font=("Helvetica", 10))
    branch_addr_label.grid(column=3, row=0)

    # branch numbers
    branch_num_label = tk.Label(staff_f1, text="Telephone Number:", font=("Helvetica", 10))
    branch_num_label.grid(column=0, row=1)
    branch_num_label = tk.Label(staff_f1, text=branch_details[0][1], font=("Helvetica", 10))
    branch_num_label.grid(column=1, row=1)


    # Staff Numbers
    branch_name_label = tk.Label(staff_f2, text="Staff Number", font=("Helvetica", 10, "bold"))
    branch_name_label.grid(column=0, row=0, padx=50)

    # Name
    branch_name_label = tk.Label(staff_f2, text="Name", font=("Helvetica", 10,"bold"))
    branch_name_label.grid(column=1, row=0, padx=50)

    # Position
    branch_name_label = tk.Label(staff_f2, text="Position", font=("Helvetica", 10,"bold"))
    branch_name_label.grid(column=2, row=0, padx=50)

    # for branch in branch_details:
    #     print(branch)

    for i in range(len(staff_details)):
        # print(f"{staff[0]}, {staff[1]}, {staff[2]}")
        # Staff Numbers
        branch_name_label = tk.Label(staff_f2, text=staff_details[i][0], font=("Helvetica", 10))
        branch_name_label.grid(column=0, row=i+1, padx=50)

        # Name
        branch_name_label = tk.Label(staff_f2, text=staff_details[i][1], font=("Helvetica", 10))
        branch_name_label.grid(column=1, row=i+1, padx=50)

        # Position
        branch_name_label = tk.Label(staff_f2, text=staff_details[i][2], font=("Helvetica", 10))
        branch_name_label.grid(column=2, row=i+1, padx=50)
    
# root = tk.Tk()
# root.title("User Details")
# root.geometry("300x200")

# details_button = tk.Button(root, text="Show User Details")

# details_button.bind("<Button-1>", lambda event: staffListing("B001"))

# details_button.grid(row=0, column=0,padx=10, pady=10)

# root.mainloop()