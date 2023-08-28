alter table orders
alter column order_date type date;

select order_no,purch_amt,order_date,customer_id,salesman_id,
		(
			select name
			from customer
			where id=customer_id
		)
from orders
where order_date='2012-08-17';