-- 1]ViewLease:

select l.lease_number, l.client_number, l.property_number, timestampdiff(MONTH, Rent_Start, Rent_Finish) AS Rent_Duration_Months 
from lease l, client c where l.client_number=c.client_number and c.Registered_By_Staff="S0001";

-- 2]propertylist:
select property_number, owner_num, is_rented from property where managed_by = "S0007";

-- 3]StaffList:
SELECT staff_number, staff_name, position FROM staff where branch_number= "B0001";
SELECT CONCAT(BStreet, ', ', BCity, ', ', BPincode) AS address, BPhone_Number FROM Branch WHERE Branch_Number = "B0001";

-- 4]WeeklyListing:
select property_number, type, CONCAT(PStreet, ', ', PCity, ', ', PPincode), rooms, rent AS address 
from property 
where Registered_At_Branch = (select Branch_Number from client where Client_Number="C0002")and Is_Rented="N";

select Branch_Number, CONCAT(BStreet, ', ', BCity, ', ', BPincode), BPhone_Number 
from branch where branch_number = (select Branch_Number from client where Client_Number="C0002" );

-- 5]UpdatingPropertyStatus:
UPDATE property SET is_rented = 'Y', SET last_rented_out = '2023-05-24' WHERE property_number = 'P0002'