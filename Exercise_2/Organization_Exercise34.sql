select salary
from worker w
where 4=(
			select count(distinct salary)
			from worker w1
			where w1.salary>w.salary
		);