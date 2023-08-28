select firstname||' '||lastname,department
from worker
where salary in(
			select max(salary)
			from worker
			group by department
			);