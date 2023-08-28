select ord.order_no,ord.order_date,ord.purch_amt,
		cust.name,cust.grade,
		sales.name,sales.commission
from orders ord
join customer cust on cust.id=ord.customer_id
join salesman sales on sales.id=ord.salesman_id
order by ord.order_no;