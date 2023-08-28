select sales.name,
		cust.name,
		cust.city
from salesman sales
join customer cust on cust.salesman_id=sales.id
group by sales.name, cust.name, cust.city
order by sales.name;