select *
from (select * 
	  from worker
	  order by id desc) as w1 
where 4>=(
		select count(id)
		from worker w2
		where w2.id>w1.id
	)
order by id;