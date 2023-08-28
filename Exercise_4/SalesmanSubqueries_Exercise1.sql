select ord.order_no,ord.purch_amt as Order_Amount,ord.order_date,cust.id as Customer_ID,sales.id as Salesman_ID
from orders ord
join salesman sales on sales.id=ord.salesman_id
join customer cust on cust.id=ord.customer_id
where sales.name='Paul Adam';