select dep.name, count(emp.id)
from emp_details emp
join emp_department dep on dep.id=emp.dpt_id
group by dep.name
having count(emp.id)>2;