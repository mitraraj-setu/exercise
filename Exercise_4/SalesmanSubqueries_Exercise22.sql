select * 
from customer
where grade>ANY(
		select grade
		from customer
		where name<'New York'
	);