select cust.name, cust.city,
		ord.order_no,ord.order_date,ord.purch_amt
from orders ord
left join customer cust on cust.id=ord.customer_id
order by cust.name;