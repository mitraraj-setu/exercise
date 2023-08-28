select sales.name as salesperson_name, sales.commission, 
		cust.name as customer_name, cust.city
from salesman sales
join customer cust on cust.salesman_id=sales.id
group by sales.name,cust.name,cust.city,sales.commission
order by cust.name;