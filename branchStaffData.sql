-- branch data
INSERT INTO Branch (Branch_Number, BStreet, BCity, BPincode, BPhone_Number) VALUES
('B001', 'Main Street', 'New York', '100101', 1234567890),
('B002', 'Broadway', 'Los Angeles', '900011', 2345678901),
('B003', 'State Street', 'Chicago', '606011', 3456789012),
('B004', 'Market Street', 'San Francisco', '194102', 4567890123),
('B005', 'Peachtree Street', 'Atlanta', '303103', 5678901234);

-- staff data
INSERT INTO staff (staff_number, staff_name, Sex, DOB, Salary, Branch_Number, Position) VALUES
('S0001', 'John Doe', 'M', '1990-01-01', 50000, 'B001', 'Manager'),
('S0002', 'Jane Smith', 'F', '1992-02-02', 45000, 'B002', 'Manager'),
('S0003', 'Mike Johnson', 'M', '1994-03-03', 40000, 'B003', 'Manager'),
('S0004', 'Sara Davis', 'F', '1996-04-04', 35000, 'B004', 'Manager'),
('S0005', 'Tom Wilson', 'M', '1998-05-05', 30000, 'B005', 'Manager'),
('S0006', 'Amy Brown', 'F', '1990-06-06', 25000, 'B001', 'Supervisor'),
('S0007', 'David Lee', 'M', '1992-07-07', 24000, 'B001', 'Assistant'),
('S0008', 'Karen Chen', 'F', '1994-08-08', 23000, 'B001', 'Assistant'),
('S0009', 'Michael Wang', 'M', '1996-09-09', 22000, 'B001', 'Assistant'),
('S0010', 'Jennifer Kim', 'F', '1998-10-10', 21000, 'B002', 'Supervisor'),
('S0011', 'Ryan Park', 'M', '1990-11-11', 20000, 'B002', 'Assistant'),
('S0012', 'Emily Lee', 'F', '1992-12-12', 19000, 'B002', 'Assistant'),
('S0013', 'Brian Davis', 'M', '1994-01-13', 18000, 'B002', 'Assistant'),
('S0014', 'Susan Lee', 'F', '1996-02-14', 17000, 'B003', 'Supervisor'),
('S0015', 'Daniel Kim', 'M', '1998-03-15', 16000, 'B003', 'Assistant'),
('S0016', 'Jessica Chen', 'F', '1990-04-16', 15000, 'B003', 'Assistant'),
('S0017', 'Kevin Wu', 'M', '1992-05-17', 14000, 'B004', 'Supervisor'),
('S0018', 'Christine Park', 'F', '1994-06-18', 13000, 'B004', 'Assistant'),
('S0019', 'Richard Lee', 'M', '1996-07-19', 12000, 'B005', 'Supervisor'),
('S0020', 'Crystal Kim', 'F', '1998-08-20', 11000, 'B005', 'Assistant');

-- manager
INSERT INTO Manager (staff_number, Manager_Start_Date, Manager_Bonus) VALUES
('S0001', '2021-01-01', 1000),
('S0002', '2021-02-01', 1200),
('S0003', '2021-03-01', 2400),
('S0004', '2021-04-01', 3000),
('S0005', '2021-05-01', 2800);

-- supervisor
-- INSERT INTO Supervisor (staff_number) VALUES
-- ('S0006'),
-- ('S0014'),
-- ('S0010'),
-- ('S0011'),
-- ('S0017'),
-- ('S0019');

-- assitant
INSERT INTO Assistant (staff_number, Supervisor_Number) VALUES
('S0007', 'S0006'),
('S0008', 'S0006'),
('S0009', 'S0006'),
('S0011', 'S0010'),
('S0012', 'S0010'),
('S0013', 'S0010'),
('S0015', 'S0014'),
('S0016', 'S0014'),
('S0018', 'S0017'),
('S0020', 'S0019');

-- owner
INSERT INTO Owner (Owner_Number, Personal_or_Business_name, Is_Business, OAddress, OCity, OPincode, Telephone_Number) VALUES
('O0001', 'John Poe', 'P', '123 Main St', 'New York', '100101', '5467382910'),
('O0002', 'Jane Doe Inc.', 'B', '456 Broadway', 'Los Angeles', '900011', '2388888901'),
('O0003', 'Peter Parker', 'P', '789 5th Ave', 'Chicago', '606011', '3477779012'),
('O0004', 'Stark Industries', 'B', '890 Park Ave', 'San Francisco', '194101', '4561190123'),
('O0005', 'Mary Lee', 'N', '555 Pine St', 'Atlanta', '303103', '2065553690');

-- property
INSERT INTO Property (Property_Number, Type, Rooms, Rent, PStreet, PCity, PPincode, Managed_By, Owner_Num, Registered_At_Branch, Is_Rented, Last_Rented_Out)
VALUES
  ('P0001', 'Flat', 2, 1200, '123 Main St', 'New York', '100101', 'S0001', 'O0001', 'B001', 'Y', '2022-03-01'),
  ('P0002', 'House', 3, 1500, '456 Park Ave', 'Los Angeles', '900011', 'S0002', 'O0002', 'B002', 'N', NULL),
  ('P0003', 'Bunglow',5, 800, '789 Broadway', 'Chicago', '606011', 'S0005', 'O0003', 'B003', 'Y', '2021-08-15'),
  ('P0004', 'Bunglow', 4, 2000, '321 Elm St', 'Atlanta', '303103', 'S0013', 'O0004', 'B005', 'N', NULL),
  ('P0005', 'House', 2, 1300, '555 Pine St', 'Atlanta', '303103', 'S0008', 'O0005', 'B005', 'Y', '2022-02-10'),
  ('P0006', 'Bunglow',4, 2500, '432 1st Ave', 'Houston', '770011', 'S0004', 'O0001', 'B004', 'N', NULL),
  ('P0007', 'Flat', 1, 900, '567 2nd St', 'Chicago', '606011', 'S0001', 'O0003', 'B003', 'Y', '2022-04-01'),
  ('P0008', 'House', 3, 1800, '789 3rd Ave', 'Los Angeles', '900011', 'S0006', 'O0004', 'B002', 'N', NULL),
  ('P0009', 'Bunglow',3, 2200, '901 4th St', 'New York', '100101', 'S0003', 'O0002', 'B001', 'Y', '2022-01-25'),
  ('P0010', 'Flat', 2, 1100, '234 5th Ave', 'Houston', '770011', 'S0010', 'O0005', 'B005', 'N', NULL);
  
  -- client
  INSERT INTO Client (Client_Number, Full_Name, Branch_Number, Registered_By_Staff, Date_Registered, PType, Max_PRent) VALUES
  ('C0001', 'Liam Wilson', 'B001', 'S0007', '2021-01-15', 'House', 1500),
  ('C0002', 'Olivia Smith', 'B002', 'S0011', '2021-02-20', 'Flat', 1300),
  ('C0003', 'Noah Johnson', 'B003', 'S0010', '2021-03-10', 'Bungalow', 2500),
  ('C0004', 'Emma Brown', 'B004', 'S0012', '2021-04-05', 'Flat', 1000),
  ('C0005', 'Ava Davis', 'B005', 'S0013', '2021-05-01', 'House', 2000),
  ('C0006', 'Liam Brown', 'B001', 'S0007', '2022-01-05', 'House', 1800),
  ('C0007', 'William Johnson', 'B002', 'S0010', '2021-11-20', 'Flat', 1200),
  ('C0008', 'Sophia Lee', 'B003', 'S0011', '2022-02-15', 'Bungalow', 2500),
  ('C0009', 'Michael Davis', 'B004', 'S0012', '2021-10-10', 'Flat', 1000),
  ('C0010', 'Isabella Wilson', 'B005', 'S0015', '2022-03-25', 'House', 2000),
  ('C0011', 'Ethan Miller', 'B001', 'S0008', '2021-12-01', 'Bungalow', 3000),
  ('C0012', 'Ava Martinez', 'B002', 'S0011', '2022-02-10', 'Flat', 1100),
  ('C0013', 'Daniel Rodriguez', 'B003', 'S0013', '2022-01-20', 'House', 1500),
  ('C0014', 'Isabella Lopez', 'B004', 'S0016', '2021-09-15', 'Bungalow', 2800),
  ('C0015', 'Matthew Hernandez', 'B005', 'S0020', '2022-04-10', 'Flat', 900);
  
  -- lease
INSERT INTO Lease (Lease_Number, Client_Number, Property_Number, Payment_method, Deposit_Paid, Rent_Start, Rent_Finish)
VALUES
  ('LS000001', 'C0001', 'P0002', 'Credit Card', 'Y', '2021-03-01', '2022-03-01'),
  ('LS000002', 'C0002', 'P0005', 'Cheque', 'Y', '2022-02-10', '2023-02-10'),
  ('LS000003', 'C0003', 'P0003', 'Cash', 'Y', '2021-08-15', '2022-08-15'),
  ('LS000004', 'C0004', 'P0007', 'Bank Transfer', 'Y', '2022-04-01', '2023-04-01'),
  ('LS000005', 'C0005', 'P0009', null, 'N', '2022-01-25', '2023-01-25'),
  ('LS000006', 'C0001', 'P0002', 'Online Transfer', 'Y', '2022-02-01', '2023-01-31'),
  ('LS000007', 'C0005', 'P0003', 'Cash', 'Y', '2021-08-15', '2022-08-14'),
  ('LS000008', 'C0003', 'P0007', null, 'N', '2022-03-01', '2023-02-28'),
  ('LS000009', 'C0002', 'P0009', 'Cash', 'Y', '2022-01-25', '2023-01-24'),
  ('LS000010', 'C0008', 'P0004', null, 'N', '2021-12-01', '2022-11-30'),
  ('LS000011', 'C0009', 'P0006', null, 'N', '2022-02-10', '2023-02-09'),
  ('LS000012', 'C0004', 'P0005', null, 'N', '2022-02-10', '2023-02-09'),
  ('LS000013', 'C0006', 'P0010', 'Cheque','Y', '2021-11-20', '2022-11-19'),
  ('LS000014', 'C0010', 'P0001', 'Online Transfer', 'Y', '2022-04-01', '2023-03-31'),
  ('LS000015', 'C0007', 'P0008', 'Cash', 'Y', '2022-01-20', '2023-01-19');


-- property report
INSERT INTO Property_Report (Property_Number, Client_Number, Comment_Date, Comment)
VALUES
  ('P0002', 'C0001', '2021-04-01', 'Good location, but noisy street.'),
  ('P0005', 'C0002', '2022-02-15', 'Nice view of the park.'),
  ('P0003', 'C0003', '2021-09-01', 'Needs some repairs.'),
  ('P0007', 'C0004', '2022-05-01', 'Clean and well-maintained.'),
  ('P0009', 'C0005', '2022-03-15', 'Spacious and comfortable.');
  

  