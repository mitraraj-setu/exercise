select grade,count(id)
from customer
group by grade,city
having grade>(
			select avg(grade)
			from customer
			where city='New York'
		);