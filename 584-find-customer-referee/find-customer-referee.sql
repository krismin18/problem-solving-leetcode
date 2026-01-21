# Write your MySQL query statement below
select name from Customer where referee_id not in (select referee_id  from Customer where referee_id=2 ) or  referee_id is null