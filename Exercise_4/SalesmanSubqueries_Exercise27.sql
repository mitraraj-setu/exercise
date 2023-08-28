select name,city, (select sum(purch_amt)
				   from orders
				   where orders.salesman_id=salesman.id
				  	)as total_order_amount
from salesman
where city in (select city
			   from customer
			  );