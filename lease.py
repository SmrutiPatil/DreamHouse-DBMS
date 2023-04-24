import mysql.connector
import os
from dotenv import load_dotenv 
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from com_function import warningWindow, connect

load_dotenv()

mysqldb = mysql.connector.connect(host="localhost", user=os.getenv("db_user"), password=os.getenv("db_password"), database=os.getenv("db_name"))
mycursor = mysqldb.cursor()

def viewlease(id, staff_dash_window):
    staff_num = id
    
    try:
        sql=("select l.lease_number, l.client_number, l.property_number, timestampdiff(MONTH, Rent_Start, Rent_Finish) AS Rent_Duration_Months from lease l, client c where l.client_number=c.client_number and c.Registered_By_Staff=%s;")
        mycursor.execute(sql, [staff_num])
        lease_details= mycursor.fetchall()
    except mysql.connector.Error as err:
        warningWindow(err)
        return
    except Exception as err:
        warningWindow(err)
        return

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
    lease_window=tk.Toplevel(staff_dash_window)
    lease_window.title("Lease Details")
    lease_window.geometry("600x500")
    lease_window.resizable(False, False)

    client_heading=tk.Frame(lease_window)
    client_heading.grid(row=0, column=0, columnspan=4, padx=10, sticky="nsew")

    client_heading_title = tk.Label(client_heading, text="Lease Form", font=("Helvetica", 15), bg="#614051", fg="white", width=50)
    client_heading_title.pack(pady=20)

    clientFrame = tk.Frame(lease_window)
    clientFrame.grid(row=1, column=0)

    clientNum = tk.Label(clientFrame, text="Client Number", font=("Helvetica", 10))
    clientNum.grid(row=1, column=0)

    clientNum_entry = tk.Entry(clientFrame, width=20)
    clientNum_entry.grid(row=1, column =1)

    clientName = tk.Label(clientFrame, text="Client Name", font=("Helvetica", 10))
    clientName.grid(row=2, column=0)

    clientName_entry = tk.Entry(clientFrame, width=20)
    clientName_entry.grid(row=2, column =1)

    propFrame = tk.Frame(lease_window)
    propFrame.grid(row=1, column=2)
    
    leaseNum = tk.Label(clientFrame, text="Lease Number", font=("Helvetica", 10))
    leaseNum.grid(row=0, column=0)

    leaseNum_entry = tk.Entry(clientFrame, width=20)
    leaseNum_entry.grid(row=0, column =1)

    propNum = tk.Label(propFrame, text="Property Number", font=("Helvetica", 10))
    propNum.grid(row=1, column=0)

    propNum_entry = tk.Entry(propFrame, width=20)
    propNum_entry.grid(row=1, column =1)

    propAddress = tk.Label(propFrame, text="Property Address", font=("Helvetica", 10))
    propAddress.grid(row=2, column=0)

    propAddress_entry = tk.Entry(propFrame, width=20)
    propAddress_entry.grid(row=2, column =1)

    payment = tk.Label(lease_window, text="Enter payment details", font=("Helvetica", 11))
    payment.grid(row=2, column=0, pady=15)

    paymentFrame = tk.Frame(lease_window)
    paymentFrame.grid(row=3, column=0)

    monthlyRent = tk.Label(paymentFrame, text="Monthly Rent", font=("Helvetica", 10))
    monthlyRent.grid(row=1, column=0)

    rentval = tk.IntVar()

    monthlyRent_entry = tk.Entry(paymentFrame, width=20, textvariable=rentval)
    monthlyRent_entry.grid(row=1, column =1)

    paymentMethod = tk.Label(paymentFrame, text="Payment Method", font=("Helvetica", 10))
    paymentMethod.grid(row=2, column=0)

    paymentMethod_entry = tk.Entry(paymentFrame, width=20)
    paymentMethod_entry.grid(row=2, column =1)

    deposit_label = tk.Label(paymentFrame, text="Deposit Paid", font=("Helvetica", 10))
    deposit_label.grid(row=3, column=0, padx=40)

    deposit_radio_frame=tk.Frame(paymentFrame)
    deposit_var = tk.StringVar()
    deposit_radio_frame.grid(row=3, column=1)
    radio_button_yes = tk.Radiobutton(deposit_radio_frame, text="Yes", value="Y", variable=deposit_var)
    radio_button_yes.pack(side="left")
    radio_button_no = tk.Radiobutton(deposit_radio_frame, text="No", value="N", variable=deposit_var)
    radio_button_no.pack(side="left")

    rentFrame = tk.Frame(lease_window)
    rentFrame.grid(row=3, column=2)

    monthlyRent = tk.Label(rentFrame, text="Rent start:", font=("Helvetica", 10))
    monthlyRent.grid(row=0, column=0)

    mngDate_entry = DateEntry(rentFrame, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
    mngDate_entry.grid(row=0, column=1)

    monthlyRent = tk.Label(rentFrame, text="Rent Finish:", font=("Helvetica", 10))
    monthlyRent.grid(row=1, column=0)

    mngDate_finish = DateEntry(rentFrame, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
    mngDate_finish.grid(row=1, column=1)
    
    def registerLease(clientFrame, propFrame, paymentFrame, rentFrame):
                db = connect()
                dbCursor = db.cursor()
                args = [leaseNum_entry.get(), clientNum_entry.get(), propNum_entry.get(), paymentMethod_entry.get(), deposit_var.get(), mngDate_entry.get_date(), mngDate_finish.get_date()]
                
                query = f"""INSERT INTO lease (lease_number, client_number, property_number, payment_method, deposit_paid, rent_start, rent_finish) 
                VALUES ('{args[0]}', '{args[1]}', '{args[2]}', '{args[3]}', '{args[4]}', '{args[5]}', '{args[6]}')"""
                
                query2 = f""""UPDATE property SET is_rented = 'Y', SET last_rented_out = '{args[6]}' WHERE property_number = '{args[2]}'"""
                
                
                try:
                    dbCursor.execute(query)
                    db.commit()
                    dbCursor.execute(query2)
                    db.commit()
                except mysql.connector.Error as err:
                    warningWindow(err)
                    return
                except Exception as err:
                    warningWindow(err)
                    return
                
                warningWindow("Lease Registered Successfully")

    submit_button = tk.Button(lease_window, text="Register", font=("Helvetica", 12), bg="#614051", fg="white", width=10)
    submit_button.bind("<Button-1>", lambda event: registerLease(clientFrame, propFrame, paymentFrame, rentFrame))
    submit_button.place(x=250, y=270)