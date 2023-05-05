create schema DreamHome;
use DreamHome;
CREATE TABLE staff(
  staff_number char(5),
  staff_name varchar(30),
  Sex char(1),
  DOB date,
  Salary numeric,
  Branch_Number char(5) references branch(branch_number),
  Position varchar(30),
  PRIMARY KEY (staff_number)
);


CREATE TABLE Manager (
  staff_number char(5) REFERENCES STAFF(STAFF_NUMBER),
  Manager_Start_Date date,
  Manager_Bonus numeric
);

-- CREATE TABLE Supervisor (
--  staff_number char(5) REFERENCES STAFF(STAFF_NUMBER)
-- );

CREATE TABLE Assistant (
  staff_number char(5) REFERENCES STAFF(STAFF_NUMBER), 
  Supervisor_Number char(5) references staff(staff_number)
);

CREATE TABLE Branch (
  Branch_Number char(5),
  BStreet varchar(30),
  BCity varchar(30),
  BPincode char(6),
  BPhone_Number numeric(10),
  PRIMARY KEY (Branch_Number)
);

CREATE TABLE Owner(
  Owner_Number char(5),
  Personal_or_Business_name varchar(30),
  Is_Business char(1),
  OAddress varchar(50),
  OCity varchar(30),
  OPincode char(6),
  Telephone_Number numeric(10),
  PRIMARY KEY (Owner_Number)
);

-- CREATE TABLE Business{
-- 	Owner_Number CHAR(5) REFERENCES OWNER(OWNER_NUMBER),
-- 	Business_Type varchar(15),
--  Contact_Name ???
-- };

CREATE TABLE Property(
  Property_Number char(5),
  Type varchar(15),
  Rooms int,
  Rent numeric,
  PStreet varchar(30),
  PCity varchar(30),
  PPincode char(6),
  Managed_By char(5) references staff(staff_number),
  Owner_Num char(5) references owner(owner_number),
  Registered_At_Branch char(5) references branch(branch_number),
  Is_Rented char,
  Last_Rented_Out date,
  PRIMARY KEY (Property_Number)
);


CREATE TABLE Client (
  Client_Number char(5),
  Full_Name varchar(30),
  Branch_Number char(5) references branch(branch_number),
  Registered_By_Staff char(5) references staff(staff_number),
  Date_Registered date,
  PType varchar(15),
  Max_PRent numeric,
  PRIMARY KEY (Client_Number)
);

CREATE TABLE Lease (
  Lease_Number char(8),
  Client_Number char(5) references client(client_number),
  Property_Number char(5) references property(property_number),
  Payment_method varchar(30),
  Deposit_Paid char,
  Rent_Start date,department
  Rent_Finish date,
  PRIMARY KEY (Lease_Number)
);

CREATE TABLE Property_Report (
  Property_Number char(5) references property(property_number),
  Client_Number char(5)references client(client_number),
  Comment_Date date,
  Comment varchar(80)
);
