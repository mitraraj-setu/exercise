select cust.name, cust.city as customer_city,
		sales.name, sales.city as salesman_city, sales.commission
from salesman sales
join customer cust on cust.salesman_id=sales.id
where cust.city != sales.city and sales.commission>0.12
order by sales.name;