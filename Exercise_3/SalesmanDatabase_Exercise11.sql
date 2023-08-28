select cust.name as customer_name, cust.city, 
		ord.order_no,ord.order_date,ord.purch_amt as Order_Amount,
		sales.name as salesman_name,sales.commission
from orders ord
left join customer cust on cust.id=ord.customer_id
left join salesman sales on sales.id=cust.salesman_id
order by ord.order_date;