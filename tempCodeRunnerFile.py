 Buttons
        staff_dash_btns=tk.Frame(staff_dash_window)
        staff_dash_btns.grid(row=1, column=0)

        staff_listing_btn = tk.Button(staff_dash_btns, text="View Staff Listing", command=staffList)
        staff_listing_btn.grid(row=0, column=0, padx=20, pady=20)
        property_listing_btn = tk.Button(staff_dash_btns, text="View Property Registered")
        property_listing_btn.grid(row=0, column=1, padx=20, pady=20)