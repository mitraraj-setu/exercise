select order_no, purch_amt, order_date, customer_id, salesman_id
from orders
where purch_amt>(
					select avg(purch_amt)
					from orders
					where order_date='2012-10-10'
				) and order_date!='2012-10-10';