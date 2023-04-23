import mysql.connector
import os
from dotenv import load_dotenv
import tkinter as tk

load_dotenv()

#function to connect with database
def connect():
    mydb = mysql.connector.connect( host= "localhost",
                                user= os.getenv("DB_USER"),
                                password= os.getenv("DB_PASSWORD"),
                                database = os.getenv("DB_NAME")
    )
    return mydb


#function to create a warning window   
def warningWindow(message):
    root = tk.Tk()
    frame1 = tk.Frame(root)
    root.title("Warning")
    root.geometry('200x75')
    
    label= tk.Label(frame1,text=message)
    label.pack()
    cancel = tk.Button(frame1,text="Cancel",command=root.destroy)
    cancel.pack()
    frame1.pack()
    
    root.mainloop()
    
    
