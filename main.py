import tkinter as tk
from tkinter import ttk
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

        elif role == "Owner":
            owner_reg_window = tk.Toplevel(self.master)
            owner_reg_window.title("Owner Registration Form")
            owner_reg_window.geometry("400x300")
            owner_reg_window.resizable(False, False)

            #labels and entries for Property registration form
            
            top_frame = Frame(owner_reg_window)
            top_frame.pack(side = "top")
            
            form_name1 = tk.Label(top_frame, text="DreamHome", font=("Helvetica", 12))
            form_name1.pack()

            form_name2 = tk.Label(top_frame, text="Property Registration Form", font=("Helvetica", 12))
            form_name2.pack()

            top_left_frame = Frame(owner_reg_window)
            top_left_frame.pack(side = LEFT)

            owner_prop_num_label = tk.Label(top_left_frame, text="Property Number: ", font=("Helvetica", 12))
            # owner_prop_num_label.pack()

            owner_prop_num_entry = tk.Entry(top_left_frame, width=30)
            # owner_prop_num_entry.pack()

            owner_prop_num_label.grid(row=1, column=1)
            owner_prop_num_entry.grid(row=1, column=2)





            








if __name__ == "__main__":
    root = tk.Tk()
    login_page = Login_Page(root)
    login_page.pack()
    root.mainloop()
