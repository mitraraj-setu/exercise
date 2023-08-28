select cust.name,cust.city,cust.grade,
		sales.name,sales.commission
from salesman sales
join customer cust on cust.salesman_id=sales.id
order by cust.id;