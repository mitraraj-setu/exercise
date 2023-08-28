select id,name,city,commission
from salesman a
where 1=(
		select count(id)
		from customer
		where salesman_id=a.id
	);