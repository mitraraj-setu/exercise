class SalesOrder:
    dict1 = {}
    def getOrder(self):
        name = input("Enter name:")
        email = input("Enter email:")
        dict1 = {"name": name,
                 "email": email,
                 "lines": []}
        response2 = input("Do you want to enter a product/(Y/N):").lower()
        if response2 == 'n':
            dict3 = {"name":name, "email":email}
            print("You entered:",dict3)
            print("Program terminated")
        while(response2 == 'y'):
            product = input("Enter product name:")
            quantity = int(input("Enter product quantity:"))
            cost = int(input("Enter product cost:"))
            dict2 = {"product":product,"quantity":quantity,"cost":cost}
            dict1.get("lines").append(dict2)
            response2 = input("Do you want to enter a product/(Y/N):").lower()
            if response2 == 'n':
                break
        print("Program Terminated!",dict1)
order1 = SalesOrder()
order1.getOrder()