select sales.name,
		cust.name,cust.city,cust.grade,
		ord.order_no,ord.order_date,ord.purch_amt
from orders ord
join customer cust on cust.id=ord.customer_id
join salesman sales on sales.id=ord.salesman_id
order by sales.name;