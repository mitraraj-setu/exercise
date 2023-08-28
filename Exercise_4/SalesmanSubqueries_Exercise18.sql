select id,name,city,commission
from salesman a
where 1<(
		select count(order_no)
		from orders
		where 1<(
				select count(customer_id)
				from orders
				where salesman_id=a.id
			)
	);