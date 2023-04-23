import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
from loginRegister import validateUser
from com_function import connect

from staffListing import staffListing
from weeklyListing import weekly_listing
from propertyRegisteredStaff import propertyList
from lease import viewlease, leaseform
from owner import ownerDashboard


class DreamHouse(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Setting up the window
        self.master = master
        self.master.title("Dreamhouse Rental Business Login")
        self.master.geometry("400x400")
        self.master.minsize(400, 400)

        self.titleframe = tk.Frame(self.master, bg="#614051")
        self.titleframe.pack(side="top", fill="x")

        self.titlelabel = tk.Label(self.titleframe, text="WELCOME TO DREAMHOUSE RENTALS", font=(
            "Helvetica", 15), bg="#614051", fg="white")
        self.titlelabel.pack(pady=20)

        self.contentframe = tk.Frame(self.master, bg="#A08C96")
        self.contentframe.pack(side="top", fill="both", expand=True)

        # Creating a label for the dropdown
        self.select_role_label = tk.Label(
            self.contentframe, text="Select Role: ", font=("Helvetica", 12), bg="#A08C96")
        self.select_role_label.place(x=20, y=10)

        # Creating a dropdown for the roles
        self.role_options = ["Staff", "Owner", "Client"]
        self.role_var = tk.StringVar()
        self.role_dropdown = ttk.Combobox(
            self.contentframe, textvariable=self.role_var, values=self.role_options, state="readonly")
        self.role_dropdown.place(x=150, y=10)

        # Creating a label for the ID entry
        self.id_label = tk.Label(
            self.contentframe, text="ID:", font=("Helvetica", 12), bg="#A08C96")
        self.id_label.place(x=20, y=40)

        # Creating an entry for the ID
        self.id_entry = tk.Entry(self.contentframe, width=23)
        self.id_entry.place(x=150, y=40)

        # Creating a button to log in
        self.login_button = tk.Button(self.contentframe, text="Log In", font=(
            "Helvetica", 12), command=self.login, bg="#614051", fg="white", width=15)
        self.login_button.place(x=100, y=100)

        self.regtitle = tk.Label(self.contentframe, text="Don't have an account?", font=(
            "Helvetica", 10), bg="#A08C96")
        self.regtitle.place(x=100, y=140)

        # Creating a button to register
        self.register_button = tk.Button(self.contentframe, text="Register", font=(
            "Helvetica", 12), command=self.register, bg="#614051", fg="white", width=10)
        self.register_button.place(x=120, y=170)

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
            staff_reg_window.geometry("600x400")
            staff_reg_window.resizable(False, False)

            # Frame for staff registration heading
            staff_heading = tk.Frame(staff_reg_window)
            staff_heading.grid(row=0, column=0, columnspan=4,
                               padx=10, sticky="nsew")

            staff_heading_title = tk.Label(staff_heading, text="Staff Registration Form", font=(
                "Helvetica", 15), bg="#614051", fg="white", width=50)
            staff_heading_title.pack(pady=20)

            # frame 1 for staff personal details
            staff_f1 = tk.Frame(staff_reg_window)
            staff_f1.grid(row=1, column=0)

            # staff name
            staff_name_label = tk.Label(
                staff_f1, text="Staff Name:", font=("Helvetica", 10))
            staff_name_label.grid(column=0, row=0)

            staff_name_entry = tk.Entry(staff_f1, width=30)
            staff_name_entry.grid(column=1, row=0)

            # staff sex
            staff_sex_label = tk.Label(
                staff_f1, text="Staff Sex:", font=("Helvetica", 10))
            staff_sex_label.grid(column=0, row=1)

            staff_sex_radio_frame = tk.Frame(staff_f1)
            staff_sex_radio_frame.grid(row=1, column=1)

            staff_sex_var = tk.StringVar()
            # staff_sex_male_radio = tk.Radiobutton(staff_sex_radio_frame, text="M", variable=staff_sex_var, value="M", command= isClicked)
            # staff_sex_female_radio = tk.Radiobutton(staff_sex_radio_frame, text="F", variable=staff_sex_var, value="F", command= isClicked)
            # staff_sex_male_radio.pack(side="left")
            # staff_sex_female_radio.pack(side="left")
            staff_sex_male_radio = tk.Radiobutton(
                staff_sex_radio_frame, text="M", variable=staff_sex_var, value="M")
            staff_sex_female_radio = tk.Radiobutton(
                staff_sex_radio_frame, text="F", variable=staff_sex_var, value="F")
            staff_sex_male_radio.pack(side="left")
            staff_sex_female_radio.pack(side="left")

            # staff dob
            dob_label = tk.Label(
                staff_f1, text="Date of Birth:", font=("Helvetica", 10))
            dob_label.grid(row=2, column=0)

            dob_entry = DateEntry(staff_f1, width=12, background='darkblue',
                                  foreground='white', date_pattern='yyyy-mm-dd')
            dob_entry.grid(row=2, column=1)

            # staff salary
            dob_label = tk.Label(staff_f1, text="Salary:",
                                 font=("Helvetica", 10))
            dob_label.grid(row=3, column=0)

            salaryval = tk.IntVar()

            staff_salary_entry = tk.Entry(
                staff_f1, width=30, textvariable=salaryval)
            staff_salary_entry.grid(column=1, row=3)

            # postion
            position_label = tk.Label(
                staff_f1, text="Position:", font=("Helvetica", 10))
            position_label.grid(column=0, row=4)

            position_entry = tk.Entry(staff_f1, width=30)
            position_entry.grid(column=1, row=4)

            # frame 2 for branch details of staff
            staff_f2 = tk.Frame(staff_reg_window)
            staff_f2.grid(row=1, column=1, padx=10)

            # staff id
            staff_id_label = tk.Label(
                staff_f2, text="Staff ID:", font=("Helvetica", 10))
            staff_id_label.grid(column=0, row=0)

            staff_id_label = tk.Label(
                staff_f2, text=id, font=("Helvetica", 10))
            staff_id_label.grid(column=1, row=0)

            # branch number
            branch_no_label = tk.Label(
                staff_f2, text="Branch Number:", font=("Helvetica", 10))
            branch_no_label.grid(column=0, row=1)

            branch_no_entry = tk.Entry(staff_f2, width=30)
            branch_no_entry.grid(column=1, row=1)

            # branch address
            branch_addr_label = tk.Label(
                staff_f2, text="Branch Address:", font=("Helvetica", 10))
            branch_addr_label.grid(column=0, row=2)

            branch_addr_entry = tk.Entry(staff_f2, width=30)
            branch_addr_entry.grid(column=1, row=2)

            # branch numbers
            branch_pnum_val = tk.IntVar()
            branch_pnum_label = tk.Label(
                staff_f2, text="Telephone Number:", font=("Helvetica", 10))
            branch_pnum_label.grid(column=0, row=3)

            branch_pnum_entry = tk.Entry(
                staff_f2, width=30, textvariable=branch_pnum_val)
            branch_pnum_entry.grid(column=1, row=3)

            # frame 3 for branch details of staff
            staff_f3 = tk.Frame(staff_reg_window)
            staff_f3.grid(row=3, column=0, pady=10)

            staff_opt_details_label = tk.Label(
                staff_f3, text="Enter details where applicable:", font=("Helvetica", 10))
            staff_opt_details_label.grid(row=0, column=0, padx=10, pady=15)

            branch_mngDate_label = tk.Label(
                staff_f3, text="Manager Start Date:", font=("Helvetica", 10))
            branch_mngDate_label.grid(column=0, row=1, padx=5)

            mngDate_entry = DateEntry(
                staff_f3, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
            mngDate_entry.grid(row=1, column=1)

            branch_mngBonus_label = tk.Label(
                staff_f3, text="Manager Bonus:", font=("Helvetica", 10))
            branch_mngBonus_label.grid(column=0, row=2)

            mngBonusval = tk.IntVar()
            branch_mngBonus_entry = tk.Entry(
                staff_f3, width=15, textvariable=mngBonusval)
            branch_mngBonus_entry.grid(column=1, row=2)

            sup_name_label = tk.Label(
                staff_f3, text="Supervisor Name:", font=("Helvetica", 10))
            sup_name_label.grid(column=0, row=3)

            branch_mngBonus_entry = tk.Entry(staff_f3, width=15)
            branch_mngBonus_entry.grid(column=1, row=3)

            def registerStaff(id, staff_f1, staff_f2):
                db = connect()
                dbCursor = db.cursor()
                args = [id, staff_name_entry.get(), staff_sex_var.get(), dob_entry.get(
                ), salaryval.get(), position_entry.get(), branch_no_entry.get()]
                query = f"""INSERT INTO staff (staff_number, staff_name, sex, dob, salary, branch_number, position)
                                VALUES ("{args[0]}", "{args[1]}", "{args[2]}", "{args[3]}", "{args[4]}", "{args[6]}", "{args[5]}")"""
                #print(query)
                dbCursor.execute(query)
                db.commit()

            # Creating a button to submit staff registration
            submit_button = tk.Button(staff_reg_window, text="Submit", font=(
                "Helvetica", 12), command=(self.staffDashboard))
            submit_button.bind(
                "<Button-1>", lambda event: registerStaff(id, staff_f1, staff_f2))
            submit_button.grid(row=4, column=0, columnspan=2, pady=15)

        if role == "Client":
            # Creating a new window for client registration
            client_reg_window = tk.Toplevel(self.master)
            client_reg_window.title("Client Registration Form")
            client_reg_window.geometry("650x350")
            client_reg_window.resizable(False, False)

            # Frame for client registration heading
            client_heading = tk.Frame(client_reg_window)
            client_heading.grid(
                row=0, column=0, columnspan=4, padx=10, sticky="nsew")

            client_heading_title = tk.Label(client_heading, text="Client Registration Form", font=(
                "Helvetica", 15), bg="#614051", fg="white", width=50)
            client_heading_title.pack(pady=20)

            # client details
            # frame
            clientDetailsFrame = tk.Frame(client_reg_window)
            clientDetailsFrame.grid(row=1, column=0)

            # # client number
            client_number_label = tk.Label(
                clientDetailsFrame, text="Client Number:", font=("Helvetica", 10))
            client_number_label.grid(row=0, column=0, padx=40)

            client_number_entry = tk.Label(clientDetailsFrame, text=id, font=("Helvetica", 10))
            client_number_entry.grid(row=0, column=1)

            # # client name
            client_name_label = tk.Label(
                clientDetailsFrame, text="Full Name:", font=("Helvetica", 10))
            client_name_label.grid(row=1, column=0, padx=40)

            client_name_entry = tk.Entry(clientDetailsFrame, width=20)
            client_name_entry.grid(row=1, column=1)

            # # client requiremnets
            # # frame
            clientRequirementsFrame = tk.Frame(client_reg_window, pady=5)
            clientRequirementsFrame.grid(row=2, column=0)

            # # property type
            clientReqHeading = tk.Label(
                clientRequirementsFrame, text="Enter property requirements:", font=("Helvetica", 10))
            clientReqHeading.grid(row=0, column=0, pady=5)

            client_Proptype_label = tk.Label(
                clientRequirementsFrame, text="Type:", font=("Helvetica", 10))
            client_Proptype_label.grid(row=1, column=0)
            client_Proptype_entry = tk.Entry(clientRequirementsFrame, width=20)
            client_Proptype_entry.grid(row=1, column=1)

            # # Max rent
            maxRent_label = tk.Label(
                clientRequirementsFrame, text="Max Rent:", font=("Helvetica", 10))
            maxRent_label.grid(row=2, column=0)

            maxRent_entry = tk.Entry(clientRequirementsFrame, width=20)
            maxRent_entry.grid(row=2, column=1)

            # frame 3 for branch details and registed by
            client_f3 = tk.Frame(client_reg_window)
            client_f3.grid(row=1, column=1, padx=20)

            # branch number
            branch_name_label = tk.Label(
                client_f3, text="Branch Number:", font=("Helvetica", 10))
            branch_name_label.grid(column=0, row=0)

            branch_name_entry = tk.Entry(client_f3, width=30)
            branch_name_entry.grid(column=1, row=0)

            # branch address
            branch_addr_label = tk.Label(
                client_f3, text="Branch Address:", font=("Helvetica", 10))
            branch_addr_label.grid(column=0, row=1, pady=5)

            branch_addr_entry = tk.Entry(client_f3, width=30)
            branch_addr_entry.grid(column=1, row=1, pady=5)

            # registed by
            registedby_label = tk.Label(
                client_f3, text="Registered By:", font=("Helvetica", 10))
            registedby_label.grid(column=0, row=2)

            registeredby_entry = tk.Entry(client_f3, width=30)
            registeredby_entry.grid(column=1, row=2)

            # date registered
            datereg_label = tk.Label(
                client_f3, text="Date Registered:", font=("Helvetica", 10))
            datereg_label.grid(column=0, row=3)

            datereg_entry = DateEntry(
                client_f3, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
            datereg_entry.grid(column=1, row=3)
            
            def registerClient(id, clientDetailsFrame, clientRequirementsFrame, client_f3):
                db = connect()
                dbCursor = db.cursor()
                args = [id, client_name_entry.get(), branch_name_entry.get(), registeredby_entry.get(), datereg_entry.get(), client_Proptype_entry.get(), maxRent_entry.get()]
                query = f"""INSERT INTO client (client_number, full_name, branch_number, registered_by_staff, Date_registered, ptype, max_prent) 
                                VALUES ("{args[0]}", "{args[1]}", "{args[2]}", "{args[3]}", "{args[4]}", "{args[5]}", "{args[6]}")"""
                #print(query)
                dbCursor.execute(query)
                db.commit()

            # Creating a button to submit client details
            submit_button = tk.Button(client_reg_window, text="Submit", font=("Helvetica", 12), command=self.clientDashboard)
            submit_button.bind("<Button-1>", lambda event: registerClient(id, clientDetailsFrame, clientRequirementsFrame, client_f3))
            submit_button.grid(row=4, column=0,columnspan=2, pady=15)

        if role == "Owner":
            # Creating a new window for staff registration
            owner_reg_window = tk.Toplevel(self.master)
            owner_reg_window.title("Owner Registration Form")
            owner_reg_window.geometry("600x350")
            owner_reg_window.resizable(False, False)

            # Frame for client registration heading
            owner_heading = tk.Frame(owner_reg_window)
            owner_heading.grid(row=0, column=0, columnspan=4,
                               padx=10, sticky="nsew")

            owner_heading_title = tk.Label(owner_heading, text="Owner Registration Form", font=(
                "Helvetica", 15), bg="#614051", fg="white", width=50)
            owner_heading_title.pack(pady=20)

            # owner details
            # frame
            ownerDetailsFrame = tk.Frame(owner_reg_window)
            ownerDetailsFrame.grid(row=1, column=0)

            # Owner details
            owner_number_label = tk.Label(
                ownerDetailsFrame, text="Owner Number:", font=("Helvetica", 10))
            owner_number_label.grid(row=0, column=0, padx=40)

            owner_number_entry = tk.Label(
                ownerDetailsFrame, text=id, font=("Helvetica", 10))
            owner_number_entry.grid(row=0, column=1)

            # # owner name
            owner_name_label = tk.Label(
                ownerDetailsFrame, text="Person/Business Name:", font=("Helvetica", 10))
            owner_name_label.grid(row=1, column=0, padx=40)

            owner_name_entry = tk.Entry(ownerDetailsFrame, width=20)
            owner_name_entry.grid(row=1, column=1)
            # # owner address
            owner_addr_label = tk.Label(ownerDetailsFrame, text="Branch Street:", font=("Helvetica", 10))
            owner_addr_label.grid(row=2, column=0, padx=40)

            owner_addr_entry = tk.Entry(ownerDetailsFrame, width=20)
            owner_addr_entry.grid(row=2, column =1)

            owner_city_label = tk.Label(ownerDetailsFrame, text="Branch City:", font=("Helvetica", 10))
            owner_city_label.grid(row=3, column=0, padx=40)

            owner_city_entry = tk.Entry(ownerDetailsFrame, width=20)
            owner_city_entry.grid(row=3, column =1)

            owner_pincode_label = tk.Label(ownerDetailsFrame, text="Branch Pincode:", font=("Helvetica", 10))
            owner_pincode_label.grid(row=4, column=0, padx=40)

            owner_pincode_entry = tk.Entry(ownerDetailsFrame, width=20)
            owner_pincode_entry.grid(row=4, column =1)

            # # telephone no
            owner_tel_val = tk.IntVar()
            owner_addr_label = tk.Label(ownerDetailsFrame, text="Tel No", font=("Helvetica", 10))
            owner_addr_label.grid(row=6, column=0, padx=40)

            owner_addr_entry = tk.Entry(ownerDetailsFrame, width=20, textvariable=owner_tel_val)
            owner_addr_entry.grid(row=6, column =1)

            def radio_button_clicked():
                owner_busiType_label = tk.Label(ownerDetailsFrame, text="Type of Business:", font=("Helvetica", 10))
                owner_busiType_label.grid(row=7, column=0, padx=40)

                owner_busiType_entry = tk.Entry(ownerDetailsFrame, width=20)
                owner_busiType_entry.grid(row=7, column =1) 

                owner_busiName_label = tk.Label(ownerDetailsFrame, text="Contact Name:", font=("Helvetica", 10))
                owner_busiName_label.grid(row=8, column=0, padx=40)

                owner_busiName_entry = tk.Entry(ownerDetailsFrame, width=20)
                owner_busiName_entry.grid(row=8, column =1)                

            owner_busi_label = tk.Label(ownerDetailsFrame, text="Personal/Business?", font=("Helvetica", 10))
            owner_busi_label.grid(row=5, column=0, padx=40)
            var = tk.StringVar()

            business_radio_frame=tk.Frame(ownerDetailsFrame)
            business_radio_frame.grid(row=5, column=1)
            radio_button_yes = tk.Radiobutton(business_radio_frame, text="Yes", value="Y",variable=var, command=radio_button_clicked)
            radio_button_yes.pack(side="left")
            radio_button_no = tk.Radiobutton(
                business_radio_frame, text="No",variable=var, value="N")
            radio_button_no.pack(side="left")

            def registerOwner(id, ownerDetailsFrame):
                db = connect()
                dbCursor = db.cursor()
                args = [id, owner_name_entry.get(), var.get(), owner_addr_entry.get(), owner_city_entry.get(), owner_pincode_entry.get(), owner_tel_val.get()]
                query = f"""INSERT INTO owner (Owner_Number, Personal_or_Business_name, Is_Business,OAddress, OCity, OPincode, Telephone_Number) 
                                VALUES ("{args[0]}", "{args[1]}", "{args[2]}", "{args[3]}", "{args[4]}", "{args[5]}", "{args[6]}")"""
                #print(query)
                dbCursor.execute(query)
                db.commit()

            # Creating a button to submit owner details
            submit_button = tk.Button(owner_reg_window, text="Submit", font=(
                "Helvetica", 12), command=self.ownerDashboard)
            submit_button.bind("<Button-1>", lambda event: registerOwner(id, ownerDetailsFrame ))
            submit_button.grid(row=3, column=0, columnspan=2, pady=15)

    def staffDashboard(self):
        # Creating a new window for staff registration
        staff_dash_window = tk.Toplevel(self.master)
        staff_dash_window.title("Staff Dashboard")
        staff_dash_window.geometry("700x400")
        staff_dash_window.resizable(False, False)

        # Frame for staff registration heading
        staff_heading = tk.Frame(staff_dash_window)
        staff_heading.grid(row=0, column=0, columnspan=6,
                           padx=10, sticky="nsew")

        staff_heading_title = tk.Label(staff_heading, text="Staff Dashboard", font=(
            "Helvetica", 15),   bg="#614051", fg="white", width=60)
        staff_heading_title.pack(pady=20)

        def staffList():
            # frame 1 for branch details
            staff_f1 = tk.Toplevel(self.master)
            staff_f1.title("Staff Listing")
            staff_f1.geometry("700x400")
            staff_f1.resizable(False, False)

            staff_Listingheading = tk.Frame(staff_f1)
            staff_Listingheading.grid(row=0, column=0, columnspan=6,
                           padx=10, sticky="nsew")

            staff_Listingheading_title = tk.Label(staff_Listingheading, text="Staff Listing", font=(
            "Helvetica", 15),   bg="#614051", fg="white", width=60)
            staff_Listingheading_title.pack(pady=20)

            # branch number
            branch_no_label = tk.Label(staff_f1, text="Branch Number: ", font=("Helvetica", 10))
            branch_no_label.place(x = 10 , y = 70)

            branch_no_entry = tk.Entry(staff_f1, width=30)
            branch_no_entry.place(x = 150 , y = 70)

            staff_details= tk.Button(staff_f1, text="Get details", font=("Helvetica", 10) ,bg="#614051", fg="white", width=10)
            staff_details.place(x = 450 , y = 60)

            staff_details.bind("<Button-1>", lambda event: staffListing(branch_no_entry, staff_f1))

            

        # Buttons
        staff_dash_btns=tk.Frame(staff_dash_window)
        staff_dash_btns.grid(row=1, column=0)

        staff_listing_btn = tk.Button(staff_dash_btns, text="View Staff Listing", font=("Helvetica", 10), bg="#614051", fg="white",command=staffList)
        staff_listing_btn.grid(row=0, column=0, padx=20, pady=20)

        property_listing_btn = tk.Button(staff_dash_btns, text="View Property Registered", font=("Helvetica", 10), bg="#614051", fg="white")
        id = self.getId()
        property_listing_btn.bind("<Button-1>", lambda event: propertyList(id, staff_dash_window))
        property_listing_btn.grid(row=0, column=1, padx=20, pady=20)

        lease_btn = tk.Button(staff_dash_btns, text="View Lease", font=("Helvetica", 10) , bg="#614051", fg="white")
        lease_btn.bind("<Button-1>", lambda event:viewlease(id, staff_dash_window))
        lease_btn.grid(row=0, column=2, padx=20, pady=20)

        lease_btn = tk.Button(staff_dash_btns, text="Lease Form", font=("Helvetica", 10) , bg="#614051", fg="white")
        lease_btn.bind("<Button-1>", lambda event:leaseform(id, staff_dash_window))
        lease_btn.grid(row=0, column=3, padx=20, pady=20)
    
    def clientDashboard(self):
        id=self.getId()
        client_dash_window = tk.Toplevel(self.master)
        client_dash_window.title("Staff Dashboard")
        client_dash_window.geometry("700x400")
        client_dash_window.resizable(False, False)

        client_heading=tk.Frame(client_dash_window)
        client_heading.grid(row=0, column=0, columnspan=6, padx=10, sticky="nsew")

        client_heading_title = tk.Label(client_heading, text="Client Dashboard", font=("Helvetica", 15),   bg="#614051", fg="white", width=60)
        client_heading_title.pack(pady=20)

        #viewed 3 things
        client_dash_btns=tk.Frame(client_dash_window)
        client_dash_btns.grid(row=1, column=0)

        prop_listing_btn = tk.Button(client_dash_btns, text="Weekly Property Listing")
        prop_listing_btn.grid(row=0, column=0, padx=20, pady=20)
        prop_listing_btn.bind("<Button-1>", lambda event:weekly_listing(id, client_dash_window))
        
        property_listing_btn = tk.Button(client_dash_btns, text="Property Viewing Report")
        property_listing_btn.grid(row=0, column=1, padx=20, pady=20)
        property_listing_btn = tk.Button(client_dash_btns, text="Lease Form")
        property_listing_btn.grid(row=0, column=2, padx=20, pady=20)
    
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
            prop_str_label = tk.Label(owner_dash_window, text="Property Street:", font=("Helvetica", 10))
            prop_str_label.grid(row=5, column=0, padx=40)

            prop_str_entry = tk.Entry(owner_dash_window, width=20)
            prop_str_entry.grid(row=5, column =1)

            prop_city_label = tk.Label(owner_dash_window, text="Property City:", font=("Helvetica", 10))
            prop_city_label.grid(row=6, column=0, padx=40)

            prop_city_entry = tk.Entry(owner_dash_window, width=20)
            prop_city_entry.grid(row=6, column =1)

            prop_pincode_label = tk.Label(owner_dash_window, text="Property Pincode:", font=("Helvetica", 10))
            prop_pincode_label.grid(row=7, column=0, padx=40)

            prop_pincode_entry = tk.Entry(owner_dash_window, width=20)
            prop_pincode_entry.grid(row=7, column =1)
            
            #rent
            prop_rent_label = tk.Label(owner_dash_window, text="Rent:", font=("Helvetica", 10))
            prop_rent_label.grid(column=0, row=8)

            prop_rent_entry = tk.Entry(owner_dash_window)
            prop_rent_entry.grid(column=1, row=8)

            # managed by
            prop_staff_label = tk.Label(owner_dash_window, text="Managed by Staff:", font=("Helvetica", 10))
            prop_staff_label.grid(column=0, row=9)
            prop_staff_entry = tk.Entry(owner_dash_window)
            prop_staff_entry.grid(column=1, row=9)

            # registered at branch
            prop_branch_label = tk.Label(owner_dash_window, text="Registed at branch:", font=("Helvetica", 10))
            prop_branch_label.grid(column=0, row=10)
            prop_branch_entry = tk.Entry(owner_dash_window)
            prop_branch_entry.grid(column=1, row=10)
            
            def registerPropertyBtn(owner_dash_window):
                db = connect()
                dbCursor = db.cursor()
                args = [prop_num_entry.get(), prop_type_entry.get(), prop_rooms_entry.get(), prop_str_entry.get(), prop_city_entry.get(), prop_pincode_entry.get(), prop_staff_entry.get(), prop_branch_entry.get(), prop_rent_entry.get()]
                query = f"""INSERT INTO property (property_number, type, rooms, pstreet, pcity, ppincode, managed_by, registered_at_branch, rent, is_rented, last_rented_out) 
                                VALUES ("{args[0]}", "{args[1]}", "{args[2]}", "{args[3]}", "{args[4]}", "{args[5]}", "{args[6]}", "{args[7]}", "{args[8]}", "N", NULL)"""
                #print(query)
                dbCursor.execute(query)
                db.commit()

            # Creating a button to submit client details
            submit_button = tk.Button(owner_dash_window, text="Submit", font=("Helvetica", 12))
            submit_button.bind("<Button-1>", lambda event: registerPropertyBtn(owner_dash_window))
            submit_button.grid(column=0, row=11, pady=20)

        prop_reg_btn=tk.Button(owner_dash_window, text="Register Property", command=registerProperty)
        prop_reg_btn.grid(row=1, column=0, pady=15)
        prop_view_btn=tk.Button(owner_dash_window, text="View registered properties")
        prop_view_btn.grid(row=1, column=1, pady=15)
                
if __name__ == "__main__":
    root = tk.Tk()
    login_page = DreamHouse(root)
    login_page.pack()
    root.mainloop()