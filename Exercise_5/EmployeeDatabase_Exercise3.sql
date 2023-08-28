select emp.firstname,
		emp.lastname,
		emp.job_id,
		dep.id,
		dep.department_name
from locations loc
join department dep on dep.location_id=loc.id
join employee emp on emp.department_id=dep.id
where loc.city='London'
order by emp.firstname;

alter table locations
add column longitude varchar(15),
add column area varchar(15);

select * from locations;

alter table locations
drop column latitude,
drop column longitude,
drop column area;

select * from locations;