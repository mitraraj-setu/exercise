select emp.firstname,emp.lastname,dep.dpt_allotment
from emp_details emp
join emp_department dep on dep.id=emp.dpt_id
where dep.dpt_allotment>50000
order by dep.dpt_allotment desc;