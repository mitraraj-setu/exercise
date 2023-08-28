select emp.firstname,emp.lastname,
		dep.name,dep.dpt_allotment
from emp_details emp
join emp_department dep on dep.id=emp.dpt_id;