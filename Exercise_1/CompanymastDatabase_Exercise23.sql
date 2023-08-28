select avg(item.pro_price)::numeric(10,2),com.name
from item_mast item
join company_mast com on com.id=item.com_id
group by com.name;