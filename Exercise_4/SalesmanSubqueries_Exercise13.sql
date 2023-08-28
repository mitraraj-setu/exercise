select order_no, purch_amt, order_date,customer_id,salesman_id
from orders
where purch_amt>=(
			select avg(purch_amt)
			from orders
	)