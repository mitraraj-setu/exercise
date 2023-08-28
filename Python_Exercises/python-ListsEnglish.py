# Initializing the list
l1 = []

#Total number of command lines
n = int(input("Enter the total number of times you want to run the commands: "))

i = 0
while(i <n):
    print("Commands: Insert, Remove, Print, Sort, Append, Pop, Reverse")
    print("Enter Exit to terminate the program")
    str = input("Enter one of the above commands:")
    str_lower = str.lower()

    if (str_lower == "print"):
        print(l1)

    elif (str_lower == "insert"):
        # print("insert ")
        loc = int(input())
        num = int(input())
        l1.insert(loc, num)
        print("Your list is:", l1)

    elif (str_lower == "remove"):
        num = int(input())
        l1.remove(num)
        print("The list after removal:", l1)

    elif (str_lower == "sort"):
        l1.sort()
        print("Your sorted list:", l1)

    elif (str_lower == "append"):
        num = int(input())
        l1.append(num)
        print("Your updated list:", l1)

    elif (str_lower == "pop"):
        l1.pop()
        print("Your list after popping:", l1)

    elif (str_lower == "reverse"):
        l1.reverse()
        print("Your reversed list:", l1)

    elif (str_lower == "exit"):
        break

    else:
        print("Invalid Command")
        continue

    i += 1