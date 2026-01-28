# Write your MySQL query statement below
select name,unique_id from employeeuni a
right join employees b
on a.id=b.id