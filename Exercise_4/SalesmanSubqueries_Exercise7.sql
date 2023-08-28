select *
from customer
where salesman_id = (
						select id
						from salesman
						where name='Mc Lyon'
					);