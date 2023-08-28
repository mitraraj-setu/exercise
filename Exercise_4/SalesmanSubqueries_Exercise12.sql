select  order_no,purch_amt,order_date,customer_id,salesman_id
from orders
where purch_amt>(
		select avg(purch_amt)
		from orders
	)
order by order_no;

SELECT * 
FROM orders a
WHERE purch_amt >
    (SELECT AVG(purch_amt) FROM orders b 
     WHERE b.customer_id = a.customer_id);