-- Write your query below
select s.seller_name 
from seller s
WHERE s.seller_id NOT IN (
    select seller_id
    from orders
    WHERE to_char(sale_date,'YYYY')='2020'
)
ORDER BY s.seller_name ASC;