select item.name,item.pro_price,com.name
from item_mast item
join company_mast com on item.com_id=com.id;