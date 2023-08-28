select ord.order_no,ord.purch_amt,ord.order_date,ord.customer_id,ord.salesman_id,
		cust.name as customer_name,cust.city as customer_city,cust.grade,
		sales.name as salesman_name,sales.city salesman_city,sales.commission
from orders ord
join customer cust on cust.id=ord.customer_id
join salesman sales on sales.id=ord.salesman_id
order by ord.order_no;