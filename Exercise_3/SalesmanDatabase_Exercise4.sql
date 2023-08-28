select cust.name,cust.city,
		sales.name,sales.commission
from salesman sales
join customer cust on cust.salesman_id=sales.id
where sales.commission>0.12
order by sales.commission desc;