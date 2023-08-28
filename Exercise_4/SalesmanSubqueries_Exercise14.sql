select sum(purch_amt),order_date
from orders 
group by order_date
having sum(purch_amt)>=(max(purch_amt)+1000)