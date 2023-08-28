create table company_mast
(
	id int PRIMARY KEY,
	name varchar(30)
);

create table item_mast
(
	id int PRIMARY KEY,
	name varchar(30),
	pro_price numeric,
	com_id int references company_mast(id)
);

insert into company_mast values
	(11,'Samsung'),
	(12,'iBall'),
	(13,'Epsion'),
	(14,'Zebronics'),
	(15,'Asus'),
	(16,'Frontech');
	
insert into item_mast values
	(101,'Mother Board',3200.00,15),
	(102,'Key Board',450.00,16),
	(103,'ZIP drive',250.00,14),
	(104,'Speaker',550.00,16),
	(105,'Monitor',5000.00,11),
	(106,'DVD drive',900.00,12),
	(107,'CD drive', 800.00,12),
	(108,'Printer',260.00,13),
	(109,'Refill cartridge',350.00,13),
	(110,'Mouse',250.00,12);

select *
from item_mast item
join company_mast com on com.id=item.com_id;