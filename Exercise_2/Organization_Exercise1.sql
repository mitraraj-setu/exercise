create table worker(
	id SERIAL PRIMARY KEY,
	firstname varchar(25) NOT NULL,
	lastname varchar(25) NOT NULL,
	salary numeric CONSTRAINT positive_salary CHECK(salary>0),
	joining_date date NOT NULL,
	department varchar(15)
);

create table bonus(
	worker_id int NOT NULL references worker(id),
	bonus_date date,
	bonus_amt numeric NOT NULL CONSTRAINT positive_bonus CHECK(bonus_amt>0)
);

create table title(
	worker_id int NOT NULL references worker(id),
	worker_title varchar NOT NULL,
	affected_from date NOT NULL 
);

INSERT INTO Worker VALUES
		(001, 'Monika', 'Arora', 100000, '2014-02-20', 'HR'),
		(002, 'Niharika', 'Verma', 80000, '2014-06-11', 'Admin'),
		(003, 'Vishal', 'Singhal', 300000, '2014-02-20', 'HR'),
		(004, 'Amitabh', 'Singh', 500000, '2014-02-20', 'Admin'),
		(005, 'Vivek', 'Bhati', 500000, '2014-06-11', 'Admin'),
		(006, 'Vipul', 'Diwan', 200000, '2014-06-11', 'Account'),
		(007, 'Satish', 'Kumar', 75000, '2014-01-20', 'Account'),
		(008, 'Geetika', 'Chauhan', 90000, '2014-04-11', 'Admin');

INSERT INTO Bonus VALUES
		(001, '2016-02-20', 5000),
		(002, '2016-06-11', 3000),
		(003, '2016-02-20', 4000),
		(001, '2016-02-20', 4500),
		(002, '2016-06-11', 3500);	

INSERT INTO Title VALUES
 (001, 'Manager', '2016-02-20'),
 (002, 'Executive', '2016-06-11'),
 (008, 'Executive', '2016-06-11'),
 (005, 'Manager', '2016-06-11'),
 (004, 'Asst. Manager', '2016-06-11'),
 (007, 'Executive', '2016-06-11'),
 (006, 'Lead', '2016-06-11'),
 (003, 'Lead', '2016-06-11');
 
select firstname as Worker_name
from worker;