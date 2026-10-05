-- Write your query below
select name from sales_person
where sales_id NOT IN 
(
    select sales_id from orders o JOIN company c on c.com_id = o.com_id
    where c.name = 'CRIMSON'
)