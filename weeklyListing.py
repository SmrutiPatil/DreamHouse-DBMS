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
    staff_num = id
    sql1=("select property_number, type, CONCAT(PStreet, ', ', PCity, ', ', PPincode), rooms, rent AS address from property where Registered_At_Branch = (select Branch_Number from client where Client_Number=%s)and Is_Rented=%s;")
    mycursor.execute(sql1, [(staff_num), ("N")])
    prop_details = mycursor.fetchall()
    
    sql2=("select Branch_Number, CONCAT(BStreet, ', ', BCity, ', ', BPincode), BPhone_Number from branch where branch_number = (select Branch_Number from client where Client_Number=%s );")
    mycursor.execute(sql2, [staff_num])
    branch_details = mycursor.fetchall()

    branch_f1=tk.Frame(client_dash_board)
    branch_f1.grid(row=2, column=0, pady=15)

    branch_num_label = tk.Label(branch_f1, text="Branch Number:", font=("Helvetica", 10))
    branch_num_label.grid(column=0, row=0)

    branch_num_entry = tk.Label(branch_f1, text=branch_details[0][0], font=("Helvetica", 10))
    branch_num_entry.grid(column=1, row=0)

    branch_addr_label = tk.Label(branch_f1, text="Branch Address:", font=("Helvetica", 10))
    branch_addr_label.grid(column=0, row=1, pady=5)

    branch_addr_entry = tk.Label(branch_f1, text=branch_details[0][1], font=("Helvetica", 10))
    branch_addr_entry.grid(column=1, row=1)
    
    branch_phone_label = tk.Label(branch_f1, text="Branch Telephone:", font=("Helvetica", 10))
    branch_phone_label.grid(column=2, row=0, pady=5)

    branch_phone_entry = tk.Label(branch_f1, text=branch_details[0][2], font=("Helvetica", 10))
    branch_phone_entry.grid(column=3, row=0)

    prop_f1=tk.Frame(client_dash_board)
    prop_f1.grid(row=3, column=0, pady=15)

    # Staff Numbers
    prop_num_label = tk.Label(prop_f1, text="Property Num", font=("Helvetica", 10, "bold"))
    prop_num_label.grid(column=0, row=0, padx=15)

    # Name
    prop_type_label = tk.Label(prop_f1, text="Type", font=("Helvetica", 10,"bold"))
    prop_type_label.grid(column=1, row=0, padx=15)

    # Position
    prop_addr_label = tk.Label(prop_f1, text="Address", font=("Helvetica", 10,"bold"))
    prop_addr_label.grid(column=2, row=0, padx=15)

    prop_rooms_label = tk.Label(prop_f1, text="Rooms", font=("Helvetica", 10,"bold"))
    prop_rooms_label.grid(column=3, row=0, padx=15)

    prop_rent_label = tk.Label(prop_f1, text="Rent", font=("Helvetica", 10,"bold"))
    prop_rent_label.grid(column=4, row=0, padx=15)

    for i in range(len(prop_details)):
        prop_num_label = tk.Label(prop_f1, text=prop_details[i][0], font=("Helvetica", 10))
        prop_num_label.grid(column=0, row=i+1, padx=15)

        # Name
        prop_type_label = tk.Label(prop_f1, text=prop_details[i][1], font=("Helvetica", 10))
        prop_type_label.grid(column=1, row=i+1, padx=15)

        # Position
        prop_addr_label = tk.Label(prop_f1, text=prop_details[i][2], font=("Helvetica", 10))
        prop_addr_label.grid(column=2, row=i+1, padx=15)

        prop_room_label = tk.Label(prop_f1, text=prop_details[i][3], font=("Helvetica", 10))
        prop_room_label.grid(column=3, row=i+1, padx=15)

        prop_rent_label = tk.Label(prop_f1, text=prop_details[i][4], font=("Helvetica", 10))
        prop_rent_label.grid(column=4, row=i+1, padx=15)

        property_listing_btn = tk.Button(prop_f1, text="Property Viewing Report")
        property_listing_btn.grid(row=i+1, column=5, padx=15)

        prop_num = prop_details[i][0]

        property_listing_btn.bind("<Button-1>", lambda event: weeklyreport(prop_num, id))
        print(i,": ",prop_details[i][0])

    def weeklyreport(prop_no, id):
        weekly_report_window=tk.Toplevel(client_dash_board)
        weekly_report_window.title("Property Viewing Report: ")
        weekly_report_window.geometry("400x400")

        prop_num_label = tk.Label(weekly_report_window, text=prop_no)
        prop_num.grid(row=0, column =0) 
      

    # property_listing_btn = tk.Button(client_dash_board, text="Property Viewing Report")
    # property_listing_btn.grid(row=4, column=0)

    # property_listing_btn.bind("<Button-1>", lambda event: weeklyreport(id, client_dash_board))



    