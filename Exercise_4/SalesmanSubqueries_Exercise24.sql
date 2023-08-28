select *
from orders
where purch_amt<any(
			select purch_amt
			from orders
			where customer_id in (
				select id
				from customer
				where city='London'
			)
		);