select *
from customer
where 1<=(
		select count(id)
		from customer
		where city='London'
	);