select * 
from orders
where purch_amt>any(
				select purch_amt
				from orders
				where order_date='2012-09-10'
			);