CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      with 
           getNthHighestSalary as (select distinct salary as sa from Employee),
           rnk as (select sa, dense_rank() over(order by sa desc) as rnk from getNthHighestSalary) 
      select max(sa) from rnk where rnk = N

  );
END