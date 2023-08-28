select order_no,purch_amt,order_date,
		salesman_id
from orders
where salesman_id in(
	select id
	from salesman
	where commission=(
		select max(commission)
		from salesman
	)
);