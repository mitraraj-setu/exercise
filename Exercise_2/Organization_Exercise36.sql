select max(salary) 
from worker
where salary not in (select max(salary) 
					 from worker);