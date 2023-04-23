import mysql.connector
import os
from dotenv import load_dotenv 
import tkinter as tk
from tkinter import ttk

load_dotenv()

mysqldb = mysql.connector.connect(host="localhost", user=os.getenv("db_user"), password=os.getenv("db_password"), database=os.getenv("db_name"))
mycursor = mysqldb.cursor()

def viewlease(id, staff_dash_window):
    staff_num = id
    sql=("select l.lease_number, l.client_number, l.property_number, timestampdiff(MONTH, Rent_Start, Rent_Finish) AS Rent_Duration_Months from lease l, client c where l.client_number=c.client_number and c.Registered_By_Staff=%s;")
    mycursor.execute(sql, [staff_num])
    lease_details= mycursor.fetchall()

    view_lease_window=tk.Toplevel(staff_dash_window)
    view_lease_window.title("Lease Details")
    view_lease_window.geometry("700x200")
    view_lease_window.resizable(False, False)

    lease_table= tk.Frame(view_lease_window)
    lease_table.grid(row=1, column=0, padx=10)

    lease_num_label = tk.Label(lease_table, text="Lease Number", font=("Helvetica", 10, "bold"))
    lease_num_label.grid(column=0, row=0, padx=25)

    client_num_label = tk.Label(lease_table, text="Client Number", font=("Helvetica", 10,"bold"))
    client_num_label.grid(column=1, row=0, padx=25)

    prop_num_label = tk.Label(lease_table, text="Property Number", font=("Helvetica", 10,"bold"))
    prop_num_label.grid(column=2, row=0, padx=25)

    rent_duration_label = tk.Label(lease_table, text="Rent Duration", font=("Helvetica", 10,"bold"))
    rent_duration_label.grid(column=3, row=0, padx=25)

    for i in range(len(lease_details)):

        lease_num_label = tk.Label(lease_table, text=lease_details[i][0], font=("Helvetica", 10))
        lease_num_label.grid(column=0, row=i+1, padx=25)

        client_num_label = tk.Label(lease_table, text=lease_details[i][1], font=("Helvetica", 10))
        client_num_label.grid(column=1, row=i+1, padx=25)

        prop_num_label = tk.Label(lease_table, text=lease_details[i][2], font=("Helvetica", 10))
        prop_num_label.grid(column=2, row=i+1, padx=25)
        
        rent_duration_label = tk.Label(lease_table, text=lease_details[i][3], font=("Helvetica", 10))
        rent_duration_label.grid(column=3, row=i+1, padx=25)

def leaseform(id, staff_dash_window):
    view_lease_window=tk.Toplevel(staff_dash_window)
    view_lease_window.title("Lease Details")
    view_lease_window.geometry("700x200")
    view_lease_window.resizable(False, False)