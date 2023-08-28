select sales.name as salesman_name,
		cust.name as customer_name,cust.grade,
		ord.purch_amt as Order_amount
from orders ord
right join customer cust on cust.id=ord.customer_id
left join salesman sales on sales.id=cust.salesman_id
where ord.purch_amt>2000 and cust.grade is not null
order by sales.name;