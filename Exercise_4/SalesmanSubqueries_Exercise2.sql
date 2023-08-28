select ord.order_no, ord.purch_amt, ord.order_date,ord.customer_id,ord.salesman_id
from orders ord
where salesman_id =(
					select sales.id
					from salesman sales
					where sales.city='London'
				);