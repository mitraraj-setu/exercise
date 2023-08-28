select *
from customer
where grade!=any(
		select grade
		from customer
		where city='London'
	);