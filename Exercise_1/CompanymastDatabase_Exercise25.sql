select  item.name,item.pro_price,com.name
from item_mast item
join company_mast com on com.id=item.com_id
and item.pro_price=(
		select max(item.pro_price)
		from item_mast item
		where item.com_id=com.id
);