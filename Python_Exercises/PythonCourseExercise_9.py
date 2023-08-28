class SalesOrder:
    dict1 = {}
    name, email, product = '','',''
    quantity = 0
    cost = 0.0
    def setOrder(self):
        name = input("Enter name:")
        email = input("Enter email:")
        product = input("Enter product name:")
        quantity = int(input("Enter product quantity:"))
        cost = int(input("Enter product cost:"))
        dict1 = {"name": name,
                 "email": email,
                 "lines": [{'product': product, 'quantity': quantity, 'cost': cost}]}
        return dict1
class GetOrder(SalesOrder):
    def getOrder(self):
        dict2 = self.setOrder()
        print("Your entered order:",dict2)

order1 = GetOrder()
order1.getOrder()