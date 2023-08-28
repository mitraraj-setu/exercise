select distinct w.id, w.salary
from worker w, worker w1
where w.salary=w1.salary
and w.id!=w1.id;