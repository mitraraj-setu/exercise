final_dict = {}
def getResponse():
    Response = input("Do you want to enter a record? (Yes/No):")
    Response_lower = Response.lower()
    if(Response_lower == "yes"):
        return True
    elif(Response_lower == "no"):
        return False
    else:
        print("Invalid response!")

while(getResponse()):
    w = input("Enter warehouse:")
    p = input("Enter product name:")
    q = input("Enter quantity name:")

    final_dict.get(w) not in final_dict and final_dict.update({w: []}) and final_dict.get(w).append({'product': p,'quantity': q}) or final_dict.get(w).append({'product':p, 'quantity': q})

    if(getResponse()):
        continue

    elif(getResponse() == False):
        print("Program Terminated!")
        break

    else:
        getResponse()
        if(getResponse()):
            continue
        elif(getResponse() == False):
            print("Program Terminated!")
            break
        else:
            print("Invalid Response!")
            print("Program Terminated!")
            break

print("Your Record:")
for x,y in final_dict.items():
    print(x,y)