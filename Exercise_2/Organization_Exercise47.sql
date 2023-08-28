select distinct salary
from worker w
where 3>(
			select count(distinct salary)
			from worker w1
			where w1.salary<w.salary
		)
order by salary;