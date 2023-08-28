select *
from salesman sales
cross join customer cust
where sales.city is not null;