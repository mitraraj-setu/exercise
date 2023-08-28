select cust.name, cust.city,
		ord.order_no,ord.order_date,ord.purch_amt
from orders ord
join customer cust on cust.id=ord.customer_id
order by ord.order_date;