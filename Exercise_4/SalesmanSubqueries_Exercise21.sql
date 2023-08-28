select * 
from salesman a
where exists(
		select name
		from customer
		where a.name<name
	);