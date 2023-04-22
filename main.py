import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *

class Login_Page(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Setting up the window
        self.master = master
        self.master.title("Dreamhouse Rental Business Login")
        self.master.geometry("400x200")
        self.master.resizable(False, False)

        # Creating a label for the dropdown
        self.select_role_label = tk.Label(self.master, text="Select Role:", font=("Helvetica", 12))
        self.select_role_label.pack(pady=10)

        # Creating a dropdown for the roles
        self.role_options = ["Staff", "Owner", "Client"]
        self.role_var = tk.StringVar()
        self.role_dropdown = ttk.Combobox(self.master, textvariable=self.role_var, values=self.role_options, state="readonly")
        self.role_dropdown.pack(pady=5)

        # Creating a label for the ID entry
        self.id_label = tk.Label(self.master, text="ID:", font=("Helvetica", 12))
        self.id_label.pack()

        # Creating an entry for the ID
        self.id_entry = tk.Entry(self.master, width=30)
        self.id_entry.pack(pady=5)

        # Creating a button to log in
        self.login_button = tk.Button(self.master, text="Log In", font=("Helvetica", 12), command=self.login)
        self.login_button.pack(pady=10)

        # Creating a button to register
        self.register_button = tk.Button(self.master, text="Register", font=("Helvetica", 12), command=self.register)
        self.register_button.pack()

    def login(self):
        role = self.role_var.get()
        id = self.id_entry.get()

        # TODO: Check if the ID is valid for the selected role and log in if it is

    def register(self):
        role = self.role_var.get()
        id = self.id_entry.get()

        # TODO: Register the ID for the selected role
        if role == "Staff":
            # Creating a new window for staff registration
            staff_reg_window = tk.Toplevel(self.master)
            staff_reg_window.title("Staff Registration Form")
            staff_reg_window.geometry("400x300")
            staff_reg_window.resizable(False, False)

            # Creating labels and entries for staff registration form
            staff_name_label = tk.Label(staff_reg_window, text="Staff Name:", font=("Helvetica", 12))
            staff_name_label.pack(pady=10)

            staff_name_entry = tk.Entry(staff_reg_window, width=30)
            staff_name_entry.pack()

            staff_sex_label = tk.Label(staff_reg_window, text="Staff Sex:", font=("Helvetica", 12))
            staff_sex_label.pack(pady=10)

            staff_sex_var = tk.StringVar()
            staff_sex_male_radio = tk.Radiobutton(staff_reg_window, text="M", variable=staff_sex_var, value="M")
            staff_sex_female_radio = tk.Radiobutton(staff_reg_window, text="F", variable=staff_sex_var, value="F")
            staff_sex_male_radio.pack()
            staff_sex_female_radio.pack()

            # Creating a button to submit staff registration
            submit_button = tk.Button(staff_reg_window, text="Submit", font=("Helvetica", 12))
            submit_button.pack(pady=10)



            # client registration form
        if role == "Client":
            # Creating a new window for staff registration
            client_reg_window = tk.Toplevel(self.master)
            client_reg_window.title("Client Registration Form")
            client_reg_window.geometry("700x500")
            client_reg_window.minsize(700 , 500)
            client_reg_window.resizable(False, False)

            # frame one at top for heading
            headingFrame = Frame(client_reg_window)
            headingFrame.pack(side="top")
        
            headingLabel = Label(headingFrame , text="Dream Home \n Client Registration Form" , bg="red" , font = "40" , fg="white" , padx="10" , pady="10")
            headingLabel.pack(side = "top", fill=Y)

            # client details
            # frame
            clientDetailsFrame = Frame(client_reg_window , bg='cyan' , width = "500" , padx=10 , pady=10)
            clientDetailsFrame.place(relx = 0, rely = 0 , x =0, y = 0, anchor = NW)
            
            # # client number
            client_number_label = Label(clientDetailsFrame, text="Client Number:", font=("Helvetica", 12))
            client_number_label.pack()

            client_number_entry = Entry(clientDetailsFrame, width=30)
            client_number_entry.pack()

            # # client name
            client_name_label = Label(clientDetailsFrame, text="Full Name:", font=("Helvetica", 12))
            client_name_label.pack()

            client_name_entry = Entry(clientDetailsFrame, width=30)
            client_name_entry.pack()


            # # client requiremnets
            # # frame
            clientRequirementsFrame = Frame(client_reg_window , bg='red' , padx=10 , pady=10)
            clientRequirementsFrame.place(relx = 0, rely = 0.5 , x =0, y = 0, anchor = SW)
            
            # # property type
            clientReqHeading = Label(clientRequirementsFrame,text="Enter property requirements" , font=("Helvetica", 18))
            clientReqHeading.pack()

            client_Proptype_label = Label(clientRequirementsFrame, text="Type:", font=("Helvetica", 12))
            client_Proptype_label.pack()

            client_Proptype_entry = Entry(clientRequirementsFrame, width=30)
            client_Proptype_entry.pack()

            # # Max rent
            maxRent_label = Label(clientRequirementsFrame, text="Full Name:", font=("Helvetica", 12))
            maxRent_label.pack()

            maxRent_entry = Entry(clientRequirementsFrame, width=30)
            maxRent_entry.pack()


            # staff_sex_label = tk.Label(client_reg_window, text="Staff Sex:", font=("Helvetica", 12))
            # staff_sex_label.pack(pady=10)

            # staff_sex_var = tk.StringVar()
            # staff_sex_male_radio = tk.Radiobutton(client_reg_window, text="M", variable=staff_sex_var, value="M")
            # staff_sex_female_radio = tk.Radiobutton(client_reg_window, text="F", variable=staff_sex_var, value="F")
            # staff_sex_male_radio.pack()
            # staff_sex_female_radio.pack()

            # Creating a button to submit staff registration
            # submit_button = tk.Button(client_reg_window, text="Submit", font=("Helvetica", 12))
            # submit_button.pack(pady=10)
        






if __name__ == "__main__":
    root = tk.Tk()
    login_page = Login_Page(root)
    login_page.pack()
    root.mainloop()
