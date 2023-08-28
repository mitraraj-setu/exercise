select avg(item.pro_price),com.name
from item_mast item
join company_mast com on com.id=item.com_id
group by com.name
having avg(item.pro_price)>=350;