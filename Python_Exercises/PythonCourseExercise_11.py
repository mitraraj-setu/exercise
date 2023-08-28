a = [{'product' : 'abc' , 'qty' : 20},
     {'product' : 'xyz' , 'qty' : 10},
     {'product' : 'gds' , 'qty' : 30},
     {'product' : 'de' , 'qty' : 100}]
def filterProductAndSort(prod):
    temp = 0
    for i in a:
        if (prod == i.get('product')):
            temp = 1
    if temp == 1:
        sorted_product = sorted(a, key=lambda x:x['product'])
        sorted_quant = sorted(a, key=lambda x:x['qty'])
        print("Sorting based on product:",sorted_product)
        print("Sorting based on quantity:",sorted_quant)

    else:
        print("Product not found!")
prod = input("Enter product name:")
filterProductAndSort(prod)