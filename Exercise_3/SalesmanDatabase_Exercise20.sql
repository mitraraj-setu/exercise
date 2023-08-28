select *
from customer cust
cross join salesman sales
where (sales.city!=cust.city) and cust.grade is not null;