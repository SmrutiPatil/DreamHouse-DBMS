alter table staff 
add foreign key(Branch_Number) references Branch(Branch_Number);

alter table Manager
add foreign key(staff_number) references staff(staff_number);

-- alter table Supervisor
-- add foreign key(staff_number) references staff(staff_number);

alter table Assistant
add foreign key(staff_number) references staff(staff_number);

alter table Property
add foreign key(Managed_By) references staff(staff_number);

alter table Property
add foreign key(Owner_Num) references Owner(Owner_Number);


alter table Property
add foreign key(Registered_At_Branch) references Branch(Branch_Number);

alter table Client 
add foreign key(Branch_Number) references Branch(Branch_Number);

alter table Client 
add foreign key(Registered_By_Staff) references staff(staff_number);

alter table Lease
add foreign key(Client_Number) references Client(Client_Number);

alter table Lease
add foreign key(Property_Number) references Property(Property_Number);

alter table Property_Report
add foreign key(Property_Number) references Property(Property_Number);

alter table Property_Report
add foreign key(Client_Number) references Client(Client_Number);
