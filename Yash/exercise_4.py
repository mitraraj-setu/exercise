l1 = [7, 9, 3]
l2 = [9, 2]
n = 100
Z = []
for x in l1:
    if x in l2:
        print(Z)
        exit()
if 0 in l2 or 0 in l1:
    print(" invalid list ")
if not l1:
    print(Z)
elif 1 in l2:
    print(Z)
elif l2 == l1:
    print(Z)
else:

    for i in range(n):
        if all(i % q == 0 for q in l1):
            if all(i % r != 0 for r in l2):
                Z.append(i)
    print(Z)
