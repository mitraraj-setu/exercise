select order_no, purch_amt, order_date, customer_id, salesman_id
from orders
where salesman_id=(
				select salesman_id
				from orders
				where customer_id=3007
			);