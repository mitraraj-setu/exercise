a = [{'product' : 'abc' , 'qty' : 20},
     {'product' : 'xyz' , 'qty' : 10},
     {'product' : 'gds' , 'qty' : 30},
     {'product' : 'de' , 'qty' : 100}]
def filter_product(prod):
     j=0
     for i in range(len(a)):
          if(prod == a[i].get('product')):
               print(a[i])
               j=j+1
     if(j!=1):
          print("Product Not Found!")

prod = input("Enter product name:")
filter(filter_product(prod),a)