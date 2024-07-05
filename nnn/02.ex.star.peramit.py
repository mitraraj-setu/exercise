#1

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#2
for i in range(1, 6):
    for j in range(1, i+1):
        print(j*2, end=" ")
    print()
#3

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j*2, end=" ")
    print()


#4
x = 1
for i in range(5, 0, -1):
    for k in range(1, x + 1):
        print(end="  ")
    for j in range(1, i + 1):
        print(j * 2, end=" ")
    print()
    x = x + 1


#5
for i in range(1, 5):
    for j in range(1, i+1):
        print(j*2-1, end=" ")
    print()
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j*2-1, end=" ")
    print()


#6 piramid.star


x = 5
for i in range(5):
    for j in range(1, i+1):
        print(j*2-1, end=" ")
    for k in range(1, x + 1):
        print(end="    ")
    for j in range(i, 1-1, -1):
        print(j*2-1, end=" ")
    print()
    x = x - 1

x = 0
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j*2-1, end=" ")
    for k in range(1, x + 1):
        print(end="    ")
    for j in range(i, 1-1, -1):
        print(j*2-1, end=" ")
    print()
    x = x + 1