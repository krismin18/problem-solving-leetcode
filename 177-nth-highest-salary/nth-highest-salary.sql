CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    declare result int;
    declare x int;
    set x = N - 1;
    set result = (
        select distinct salary from
        employee 
        order by salary desc
        limit x, 1
    );
    return result;
END