select *
from customer a
where grade not in(
			select grade
			from customer b
			where city='Paris'
		);