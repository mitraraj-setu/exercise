select *
from orders
where purch_amt<(select max(purch_amt)
				 from orders a,customer b
				 where a.customer_id=b.id and
						city='London'
				);