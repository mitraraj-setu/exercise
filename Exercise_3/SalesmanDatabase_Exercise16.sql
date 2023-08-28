select cust.name, cust.city,
		ord.order_no, ord.order_date, ord.purch_amt 
from orders ord
full outer join customer cust on cust.id=ord.customer_id
where cust.grade is not null
order by cust.name;