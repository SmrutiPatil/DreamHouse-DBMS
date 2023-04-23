            owner_busi_label = tk.Label(ownerDetailsFrame, text="Personal/Business?", font=("Helvetica", 10))
            owner_busi_label.grid(row=4, column=0, padx=40)

            business_radio_frame=tk.Frame(ownerDetailsFrame)
            business_radio_frame.grid(row=4, column=1)
            radio_button_yes = tk.Radiobutton(business_radio_frame, text="Yes", value="Y", command=radio_button_clicked)
            radio_button_yes.pack(side="left")
            radio_button_no = tk.Radiobutton(business_radio_frame, text="No", value="N")
            radio_button_no.pack(side="left")