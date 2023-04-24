#QUERY SHEET 2

#  List details of staff supervised by a named Supervisor at the branch.
select x.staff_name 
from staff x, assistant a, staff s
where s.staff_name = "Amy Brown" and a.supervisor_number = s.staff_number and x.staff_number = a.staff_number;
 
#List details of all Assistants alphabetically by name at the branch.
select s.staff_number,s.staff_name,position,s.Branch_Number 
from staff s
natural join assistant
where Branch_Number="B001"
order by staff_name;
 
#List the details of property (including the rental deposit) available for rent at the branch, along with the owner’s details.
select distinct property_number, concat_ws(" ",Pstreet, pcity, ppincode), managed_by, Owner_num, Registered_at_branch, is_rented, last_rented_out, is_business, telephone_number
from property p
join owner o on p.Owner_Num=o.Owner_Number
where p.Registered_At_Branch="B005" and p.Is_Rented="N";
 
#List the details of properties managed by a named member of staff at the branch.
select p.property_number,Pstreet,PCity,PPincode,type,rent,managed_by,staff_name,owner_num,registered_at_branch
from property p
join staff s on p.Managed_By=s.staff_number
where Registered_At_Branch="B003" and staff_name="John Doe";
 
 # List the clients registering at the branch and the names of the members of staff who registered the clients.
 select client_number,full_name,registered_by_staff,staff_name,c.branch_number
 from client c,staff s
 where c.Branch_Number="B001"
 and c.Registered_By_Staff=s.staff_number;
 
 
 #Identify properties located in Seattle with rents no higher than £450.
select p.property_number,Pstreet,PCity,PPincode,type,rent,managed_by,owner_num,registered_at_branch,BCity
from property p,branch b 
where p.Registered_At_Branch=b.Branch_Number and b.BCity="New York" and rent<1500;
 
 
# Identify the name and telephone number of an owner of a given property.
select property_number,PStreet,PCity,owner_num,Personal_or_Business_name,Telephone_number
from property p
join owner o on owner_num = owner_number;

#List the details of comments made by clients viewing a given property.
select * from property_report where Property_Number="P0003";

# Display the names and phone numbers of clients who have viewed a given property but not supplied comments.
select Full_Name,c.Client_Number 
from client c 
where c.Client_Number in (select Client_Number from property_report where comment=null);

# Display the details of a lease between a named client and a given property.
select lease_number,l.property_number,full_name
from property p, lease l,client c 
where p.Property_Number="P0004" and c.Client_Number=l.Client_Number and full_name = "Sophia Lee";

#Identify the leases due to expire next month at the branch.
Select *
from lease natural join property
where rent_finish between curdate() and curdate()+1 and registered_at_branch = "B001";

#List the details of properties that have not been rented out for more than three months.
Select *
from property
where abs(timestampdiff(MONTH,curdate(),last_rented_out)) > 3;

#Produce a list of clients whose preferences match a particular property.
select distinct client_number,full_name,Ptype 
from property p,client c
where c.PType=p.Type and c.Max_PRent<=p.Rent;



