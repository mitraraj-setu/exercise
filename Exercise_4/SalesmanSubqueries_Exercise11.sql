select a.id, a.name
from salesman a
where 1<(
		select count(id)
		from customer
		where salesman_id=a.id
	);