SELECT *
FROM salesman 
WHERE city=ANY
    (SELECT city
     FROM customer);