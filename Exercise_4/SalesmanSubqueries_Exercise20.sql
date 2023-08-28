select *
from salesman
where city in (
			select city
			from customer 
	);