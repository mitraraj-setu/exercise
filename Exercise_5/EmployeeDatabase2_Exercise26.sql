create table emp_department(
	id int PRIMARY KEY,
	name varchar(30),
	dpt_allotment numeric
);

create table emp_details(
	id int PRIMARY KEY,
	firstname varchar(15),
	lastname varchar(15),
	dpt_id int references emp_department(id)
);

insert into emp_department values
	(57,'IT',65000),
	(63,'Finance',15000),
	(47,'HR',240000),
	(27,'RD',55000),
	(89,'QC',75000);
	
insert into emp_details values
	(127323,'Michale ','Robbin   ',57),
	(526689,'Carlos  ','Snares   ',63),
	(843795,'Enric   ','Dosio    ',57),
	(328717,'Jhon    ','Snares   ',63),
	(444527,'Joseph  ','Dosni    ',47),
	(659831,'Zanifer ','Emily    ',47),
	(847674,'Kuleswar','Sitaraman',57),
	(748681,'Henrey  ','Gabriel  ',47),
	(555935,'Alex    ','Manuel   ',57),
	(539569,'George  ','Mardy    ',27),
	(733843,'Mario   ','Saule    ',63),
	(631548,'Alan    ','Snappy   ',27),
	(839139,'Maria   ','Foster   ',57);
	
select emp.id, emp.firstname,emp.lastname,emp.dpt_id,dep.name
from emp_details emp
join emp_department dep on dep.id=emp.dpt_id;
