import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
from loginRegister import validateUser

from staffListing import staffListing
from propertyRegisteredStaff import propertyList
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
        flag = validateUser(role, id)

        if flag:
            if role == "Staff":
                self.staffDashboard()
            elif role == "Client":
                self.clientDashboard()
            elif role == "Owner":
                self.ownerDashboard()

    def getId(self):
        id = self.id_entry.get()
        return id
    
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
            staff_salary_entry = tk.Entry(staff_f1, width=30, textvariable=salaryval)
            staff_salary_entry.grid(column=1, row=3)

            # postion
            position_label = tk.Label(staff_f1, text="Position:", font=("Helvetica", 10))
            position_label.grid(column=0, row=4)

            position_entry = tk.Entry(staff_f1, width=30)
            position_entry.grid(column=1, row=4)

            # frame 2 for branch details of staff
            staff_f2= tk.Frame(staff_reg_window)
            staff_f2.grid(row=1, column=1, padx=10)
            
            #staff id
            staff_id_label = tk.Label(staff_f2, text="Staff ID:", font=("Helvetica", 10))
            staff_id_label.grid(column=0, row=0)
            
            staff_id_label = tk.Label(staff_f2, text=id, font=("Helvetica", 10))
            staff_id_label.grid(column=1, row=0)
            
            # branch number
            branch_no_label = tk.Label(staff_f2, text="Branch Number:", font=("Helvetica", 10))
            branch_no_label.grid(column=0, row=1)

            branch_no_entry = tk.Entry(staff_f2, width=30)
            branch_no_entry.grid(column=1, row=1)

            # branch address
            branch_addr_label = tk.Label(staff_f2, text="Branch Address:", font=("Helvetica", 10))
            branch_addr_label.grid(column=0, row=2)

            branch_addr_entry = tk.Entry(staff_f2, width=30)
            branch_addr_entry.grid(column=1, row=2)

            # branch numbers
            branch_pnum_val = tk.IntVar()
            branch_pnum_label = tk.Label(staff_f2, text="Telephone Number:", font=("Helvetica", 10))
            branch_pnum_label.grid(column=0, row=3)

            branch_pnum_entry = tk.Entry(staff_f2, width=30, textvariable=branch_pnum_val)
            branch_pnum_entry.grid(column=1, row=3)

            # frame 3 for branch details of staff
            staff_f3= tk.Frame(staff_reg_window)
            staff_f3.grid(row=3, column=0, pady=10)

            staff_opt_details_label= tk.Label(staff_f3, text="Enter details where applicable:", font=("Helvetica", 10))
            staff_opt_details_label.grid(row=0, column=0, padx=10, pady=15)

            branch_mngDate_label = tk.Label(staff_f3, text="Manager Start Date:", font=("Helvetica", 10))
            branch_mngDate_label.grid(column=0, row=1, padx=5)

            mngDate_entry = DateEntry(staff_f3, width=12, background='darkblue',foreground='white', date_pattern='yyyy-mm-dd')
            mngDate_entry.grid(row=1, column=1)

            branch_mngBonus_label = tk.Label(staff_f3, text="Manager Bonus:", font=("Helvetica", 10))
            branch_mngBonus_label.grid(column=0, row=2)
            
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
            submit_button = tk.Button(staff_reg_window, text="Submit", font=("Helvetica", 12), command=self.staffDashboard)
            submit_button.grid(row=4, column=0,columnspan=2, pady=15)

        if role == "Client":
            # Creating a new window for staff registration
            client_reg_window = tk.Toplevel(self.master)
            client_reg_window.title("Client Registration Form")
            client_reg_window.geometry("650x350")
            client_reg_window.resizable(False, False)

            # Frame for client registration heading
            client_heading=tk.Frame(client_reg_window)
            client_heading.grid(row=0, column=0, columnspan=4, padx=10, sticky="nsew")

            client_heading_title = tk.Label(client_heading, text="Client Registration Form", font=("Helvetica", 15), bg="#614051", fg="white", width=50)
            client_heading_title.pack(pady=20)

            # client details
            # frame
            clientDetailsFrame = tk.Frame(client_reg_window)
            clientDetailsFrame.grid(row=1, column=0)
            
            # # client number
            client_number_label = tk.Label(clientDetailsFrame, text="Client Number:", font=("Helvetica", 10))
            client_number_label.grid(row=0, column=0, padx=40)

            client_number_entry = tk.Entry(clientDetailsFrame, width=20)
            client_number_entry.grid(row=0, column=1)

            # # client name
            client_name_label = tk.Label(clientDetailsFrame, text="Full Name:", font=("Helvetica", 10))
            client_name_label.grid(row=1, column=0, padx=40)

            client_name_entry = tk.Entry(clientDetailsFrame, width=20)
            client_name_entry.grid(row=1, column =1)


            # # client requiremnets
            # # frame
            clientRequirementsFrame = tk.Frame(client_reg_window, pady=5)
            clientRequirementsFrame.grid(row=2, column = 0)
            
            # # property type
            clientReqHeading = tk.Label(clientRequirementsFrame,text="Enter property requirements:" , font=("Helvetica", 10))
            clientReqHeading.grid(row=0, column =0, pady=5)

            client_Proptype_label = tk.Label(clientRequirementsFrame, text="Type:", font=("Helvetica", 10))
            client_Proptype_label.grid(row=1, column = 0)
            client_Proptype_entry = tk.Entry(clientRequirementsFrame, width=20)
            client_Proptype_entry.grid(row=1, column = 1)

            # # Max rent
            maxRent_label = tk.Label(clientRequirementsFrame, text="Max Rent:", font=("Helvetica", 10))
            maxRent_label.grid(row=2, column = 0)

            maxRent_entry = tk.Entry(clientRequirementsFrame, width=20)
            maxRent_entry.grid(row=2, column = 1)

            # frame 3 for branch details and registed by
            client_f3= tk.Frame(client_reg_window)
            client_f3.grid(row=1, column=1, padx=20)
            
            # branch number
            branch_name_label = tk.Label(client_f3, text="Branch Number:", font=("Helvetica", 10))
            branch_name_label.grid(column=0, row=0)

            branch_name_entry = tk.Entry(client_f3, width=30)
            branch_name_entry.grid(column=1, row=0)

            # branch address
            branch_addr_label = tk.Label(client_f3, text="Branch Address:", font=("Helvetica", 10))
            branch_addr_label.grid(column=0, row=1, pady=5)

            branch_addr_entry = tk.Entry(client_f3, width=30)
            branch_addr_entry.grid(column=1, row=1, pady=5)

            # registed by
            registedby_label = tk.Label(client_f3, text="Registered By:", font=("Helvetica", 10))
            registedby_label.grid(column=0, row=2)

            registeredby_entry = tk.Entry(client_f3, width=30)
            registeredby_entry.grid(column=1, row=2)

            # date registered
            datereg_label = tk.Label(client_f3, text="Date Registered:", font=("Helvetica", 10))
            datereg_label.grid(column=0, row=3)

            datereg_entry = DateEntry(client_f3, width=12, background='darkblue',foreground='white', date_pattern='yyyy-mm-dd')
            datereg_entry.grid(column=1, row=3)

            # Creating a button to submit client details
            submit_button = tk.Button(client_reg_window, text="Submit", font=("Helvetica", 12), command=self.clientDashboard())
            submit_button.grid(row=4, column=0,columnspan=2, pady=15)

        if role == "Owner":
            # Creating a new window for staff registration
            owner_reg_window = tk.Toplevel(self.master)
            owner_reg_window.title("Owner Registration Form")
            owner_reg_window.geometry("600x350")
            owner_reg_window.resizable(False, False)

            # Frame for client registration heading
            owner_heading=tk.Frame(owner_reg_window)
            owner_heading.grid(row=0, column=0, columnspan=4, padx=10, sticky="nsew")

            owner_heading_title = tk.Label(owner_heading, text="Owner Registration Form", font=("Helvetica", 15), bg="#614051", fg="white", width=50)
            owner_heading_title.pack(pady=20)

            # owner details
            # frame
            ownerDetailsFrame = tk.Frame(owner_reg_window)
            ownerDetailsFrame.grid(row=1, column=0)

            # Owner details
            owner_number_label = tk.Label(ownerDetailsFrame, text="Owner Number:", font=("Helvetica", 10))
            owner_number_label.grid(row=0, column=0, padx=40)

            owner_number_entry = tk.Entry(ownerDetailsFrame, width=20)
            owner_number_entry.grid(row=0, column=1)

            # # owner name
            owner_name_label = tk.Label(ownerDetailsFrame, text="Person/Business Name:", font=("Helvetica", 10))
            owner_name_label.grid(row=1, column=0, padx=40)

            owner_name_entry = tk.Entry(ownerDetailsFrame, width=20)
            owner_name_entry.grid(row=1, column =1)
            # # owner address
            owner_addr_label = tk.Label(ownerDetailsFrame, text="Address:", font=("Helvetica", 10))
            owner_addr_label.grid(row=2, column=0, padx=40)

            owner_addr_entry = tk.Entry(ownerDetailsFrame, width=20)
            owner_addr_entry.grid(row=2, column =1)

            # # telephone no
            owner_tel_val = tk.IntVar()
            owner_addr_label = tk.Label(ownerDetailsFrame, text="Tel No", font=("Helvetica", 10))
            owner_addr_label.grid(row=3, column=0, padx=40)

            owner_addr_entry = tk.Entry(ownerDetailsFrame, width=20, textvariable=owner_tel_val)
            owner_addr_entry.grid(row=3, column =1)

            def radio_button_clicked():
                owner_busiType_label = tk.Label(ownerDetailsFrame, text="Type of Business:", font=("Helvetica", 10))
                owner_busiType_label.grid(row=5, column=0, padx=40)

                owner_busiType_entry = tk.Entry(ownerDetailsFrame, width=20)
                owner_busiType_entry.grid(row=5, column =1) 

                owner_busiName_label = tk.Label(ownerDetailsFrame, text="Contact Name:", font=("Helvetica", 10))
                owner_busiName_label.grid(row=6, column=0, padx=40)

                owner_busiName_entry = tk.Entry(ownerDetailsFrame, width=20)
                owner_busiName_entry.grid(row=6, column =1)                

            owner_busi_label = tk.Label(ownerDetailsFrame, text="Personal/Business?", font=("Helvetica", 10))
            owner_busi_label.grid(row=4, column=0, padx=40)

            business_radio_frame=tk.Frame(ownerDetailsFrame)
            business_radio_frame.grid(row=4, column=1)
            radio_button_yes = tk.Radiobutton(business_radio_frame, text="Yes", value="Y", command=radio_button_clicked)
            radio_button_yes.pack(side="left")
            radio_button_no = tk.Radiobutton(business_radio_frame, text="No", value="N")
            radio_button_no.pack(side="left")

            # Creating a button to submit owner details
            submit_button = tk.Button(owner_reg_window, text="Submit", font=("Helvetica", 12), command=self.ownerDashboard)
            submit_button.grid(row=3, column=0,columnspan=2, pady=15)
            
    def staffDashboard(self):
        # Creating a new window for staff registration
        staff_dash_window = tk.Toplevel(self.master)
        staff_dash_window.title("Staff Dashboard")
        staff_dash_window.geometry("700x400")
        staff_dash_window.resizable(False, False)

        # Frame for staff registration heading
        staff_heading=tk.Frame(staff_dash_window)
        staff_heading.grid(row=0, column=0, columnspan=6, padx=10, sticky="nsew")

        staff_heading_title = tk.Label(staff_heading, text="Staff Dashboard", font=("Helvetica", 15),   bg="#614051", fg="white", width=60)
        staff_heading_title.pack(pady=20)

        def staffList():
            # frame 1 for branch details
            staff_f1= tk.Frame(staff_dash_window)
            staff_f1.grid(row=2, column=0, padx=10)
                
            # branch number
            branch_no_label = tk.Label(staff_f1, text="Branch Number:", font=("Helvetica", 10))
            branch_no_label.grid(column=0, row=0)

            branch_no_entry = tk.Entry(staff_f1, width=30)
            branch_no_entry.grid(column=1, row=0)

            staff_details= tk.Button(staff_dash_window, text="Get details")
            staff_details.grid(column=0, row=3, columnspan=4)

            staff_details.bind("<Button-1>", lambda event: staffListing(branch_no_entry, staff_f1, staff_f2))

            staff_f2= tk.Frame(staff_dash_window)
            staff_f2.grid(row=4, column=0, pady=15)    

        # Buttons
        staff_dash_btns=tk.Frame(staff_dash_window)
        staff_dash_btns.grid(row=1, column=0)

        staff_listing_btn = tk.Button(staff_dash_btns, text="View Staff Listing", command=staffList)
        staff_listing_btn.grid(row=0, column=0, padx=20, pady=20)
        property_listing_btn = tk.Button(staff_dash_btns, text="View Property Registered")
        id = self.getId()
        property_listing_btn.bind("<Button-1>", lambda event: propertyList(id, staff_dash_window))

        property_listing_btn.grid(row=0, column=1, padx=20, pady=20)
        property_listing_btn = tk.Button(staff_dash_btns, text="Lease Form")
        property_listing_btn.grid(row=0, column=2, padx=20, pady=20)
    
    def clientDashboard(self):
        pass
    
    def ownerDashboard(self):
        owner_dash_window = tk.Toplevel(self.master)
        owner_dash_window.title("Owner Dashboard")
        owner_dash_window.geometry("600x400")
        owner_dash_window.resizable(False, False)

        owner_heading=tk.Frame(owner_dash_window)
        owner_heading.grid(row=0, column=0, columnspan=4, padx=10, sticky="nsew")

        owner_heading_title = tk.Label(owner_heading, text="Owner Dashboard", font=("Helvetica", 15), bg="#614051", fg="white", width=50)
        owner_heading_title.pack(pady=20)

        def registerProperty():
            # Staff Numbers
            prop_num_label = tk.Label(owner_dash_window, text="Property Number:", font=("Helvetica", 10))
            prop_num_label.grid(column=0, row=2)
            
            prop_num_entry = tk.Entry(owner_dash_window)
            prop_num_entry.grid(column=1, row=2)

            # Type
            prop_type_label = tk.Label(owner_dash_window, text="Type:", font=("Helvetica", 10))
            prop_type_label.grid(column=0, row=3)

            prop_type_entry = tk.Entry(owner_dash_window)
            prop_type_entry.grid(column=1, row=3)

            # Rooms
            prop_rooms_label = tk.Label(owner_dash_window, text="Rooms:", font=("Helvetica", 10))
            prop_rooms_label.grid(column=0, row=4)
            prop_rooms_entry = tk.Entry(owner_dash_window)
            prop_rooms_entry.grid(column=1, row=4)

            # Address
            prop_addr_label = tk.Label(owner_dash_window, text="Address", font=("Helvetica", 10))
            prop_addr_label.grid(column=0, row=5, pady=15)
            prop_addr_entry = tk.Entry(owner_dash_window)
            prop_addr_entry.grid(column=1, row=5, pady=15)

            # managed by
            prop_staff_label = tk.Label(owner_dash_window, text="Managed by Staff:", font=("Helvetica", 10))
            prop_staff_label.grid(column=0, row=6)
            prop_staff_entry = tk.Entry(owner_dash_window)
            prop_staff_entry.grid(column=1, row=6)

            # managed by
            prop_branch_label = tk.Label(owner_dash_window, text="Registed at branch:", font=("Helvetica", 10))
            prop_branch_label.grid(column=0, row=7)
            prop_branch_entry = tk.Entry(owner_dash_window)
            prop_branch_entry.grid(column=1, row=7)

        prop_reg_btn=tk.Button(owner_dash_window, text="Register Property", command=registerProperty)
        prop_reg_btn.grid(row=1, column=0, pady=15)
        prop_view_btn=tk.Button(owner_dash_window, text="View registered properties")
        prop_view_btn.grid(row=1, column=1, pady=15)
                
if __name__ == "__main__":
    root = tk.Tk()
    login_page = Login_Page(root)
    login_page.pack()
    root.mainloop()