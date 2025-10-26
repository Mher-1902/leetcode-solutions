select COALESCE ((with tempo as (select distinct salary as SecondHighestSalary 
from Employee),
    ranked as (
        select dense_rank() over(order by SecondHighestSalary  desc) as rnk,SecondHighestSalary 
        from tempo
    )
select SecondHighestSalary  
from ranked
where rnk = 2),NULL) as SecondHighestSalary