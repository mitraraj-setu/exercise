select order_no, purch_amt, order_date, customer_id,salesman_id
from orders
where salesman_id=(
				select id
				from salesman
				where city='New York'
			);