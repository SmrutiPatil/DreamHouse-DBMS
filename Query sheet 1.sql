#Query Sheet 1

#details of branches in a city
select * from branch where BCity="Chicago";

#Total Number of branches from each city
SELECT BCity, COUNT(*) AS Num_Branches
FROM Branch
GROUP BY BCity;

#List the name, position, and salary of staff at a given branch, ordered by staff name.
select staff_name, salary, position 
from staff
where branch_number = "B001"
order by staff_name;

#Identify the total number of staff and the sum of their salaries.
select branch_number as branch, sum(salary) as Total_salary_of_staff, count(staff_number) as Number_of_staff 
from staff 
group by staff.Branch_Number;

#Identify the total number of staff in each position at branches in New York.
SELECT COUNT(staff_number) AS total_staff, Position
FROM staff
WHERE Branch_Number IN (SELECT Branch_Number FROM branch WHERE Bcity='New York')
GROUP BY Position;

#List the name of each Manager at each branch, ordered by branch address.
select s.staff_name, b.Branch_Number, b.BStreet, b.BCity 
from staff s
inner join branch b on s.branch_number=b.branch_number
where s.Position="Manager"
order by b.BStreet,b.BCity;

# List the names of staff supervised by a named Supervisor.
select x.staff_name 
from staff x, assistant a, staff s
where s.staff_name = "Amy Brown" and a.supervisor_number = s.staff_number and x.staff_number = a.staff_number;

#List the property number, address, type, and rent of all properties in Glasgow, ordered by rental amount
select property_number, concat_ws(" ",PStreet, PCity, PPincode) as Address, rent 
from property, branch
where BCity="New York" and Branch_Number=Registered_At_Branch
order by rent;

# List the details of properties for rent managed by a named member of staff
select property_number, concat_ws(" ", PStreet,PCity,PPincode) as address, type, rent,managed_by,staff_name, owner_num, registered_at_branch, is_rented, Last_rented_out
from property p, staff s 
where s.staff_name="John Doe"
and s.staff_number=p.Managed_By;

# Identify the total number of properties assigned to each member of staff at a given branch.
select s.staff_number, count(distinct property_number) as number_of_properties, b.branch_number
from property p,staff s,branch b 
where p.Registered_At_Branch=b.Branch_Number and b.Branch_Number="B005" and p.Managed_By=s.staff_number 
group by s.staff_number;


# List the details of properties provided by business owners at a given branch.
select property_number, concat_ws(" ",PStreet,PCity,PPincode) as address,type,rent 
from property p, owner o
where p.Registered_At_Branch="B001" and o.owner_number=p.Owner_Num and o.Is_Business='B';


#Identify the total number of properties of each type at all branches.
select count(property_number) as Number_of_Properties, type 
from property 
group by type;

# Identify the details of private property owners that provide more than one property for rent.
SELECT Owner_Number,Personal_or_Business_name, concat_ws(" ",OAddress,OCity,OPincode) as address
FROM owner
JOIN property ON property.owner_num = owner.Owner_Number
WHERE owner.Is_Business = "P"
GROUP BY owner.Owner_Number
HAVING COUNT(property.Property_Number) > 1;


# Identify flats with at least three rooms and with a monthly rent no higher than £1500 in atlanta.
select property_number,concat_ws(" ", Pstreet, PCity, PPincode) as address, type,rent,managed_by,owner_num,registered_at_branch,is_rented,Last_rented_out
 from property,branch
 where type="flat" and rooms>=3 and rent<1500 and Registered_At_Branch=Branch_Number and BCity="Atlanta";
 
#List the number, name, and telephone number of clients and their property preferences at a given branch.
 select Client_Number, full_name, PType, Max_PRent 
 from branch, client 
 where branch.Branch_Number=client.Branch_Number
 and branch.Branch_Number="B001";


#Identify the properties that have been advertised more than the average number of times.

#List the details of leases due to expire next month at a given branch.
Select *
from lease
where rent_finish between curdate() and curdate()+1;


# List the total number of leases with rental periods that are less than one year at branches in New York.
select count(lease_number)
from lease
natural join property, branch
where datediff(rent_finish, rent_start) < 365 and registered_at_branch = branch_number and bcity = "New York";

# List the total possible daily rental for property at each branch, ordered by branch number.
select avg(rent), registered_at_branch as branch_number
from property
group by registered_at_branch
order by registered_at_branch;

