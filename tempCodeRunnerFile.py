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