select *
from customer cust
cross join salesman sales
where sales.city is not null and cust.grade is not null;