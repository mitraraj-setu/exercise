select *
from customer a
where grade>all(
		select grade
		from customer b
		where city='New York' 	
	);