select cust.name, cust.city,cust.grade,
		sales.name,sales.city
from salesman sales
join customer cust on cust.salesman_id=sales.id
where cust.grade<300
order by cust.id;