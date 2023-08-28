select sales.id,sales.name as salesman_name,cust.name as customer_name
from salesman sales
left join customer cust on cust.salesman_id=sales.id
order by sales.id;