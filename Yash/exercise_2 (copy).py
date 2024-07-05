# 1
def num(n):
    for i in range(n + 2):
        for j in range(1, i):
            print(j, end=" ")
        print()


num(5)


# 2
def num(n):
    for i in range(n + 2):
        for j in range(1, i):
            print(j * 2, end=" ")
        print()


num(5)
print()


# 3
def num(n):
    for i in range(n + 1, 0, -1):
        for j in range(1, i):
            print(j * 2, end=" ")
        print()


num(5)


# 4
def num(n):
    for i in range(n + 1, 0, -1):
        space = ((n + 2 - i) - 1)
        for k in range(space):
            print("  ", end="")
        for j in range(1, i):
            print(j * 2, end=" ")
        print()


num(5)


# 5
def num(n):
    for i in range(n + 1):
        for j in range(1, i * 2, 2):
            print(j, end=" ")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(1, i * 2, 2):
            print(j, end=" ")
        print()


num(5)
print()


# 6
def num(n):
    for i in range(1, n + 1):
        for j in range(1, i * 2, 2):
            print(j, end=" ")
        space = (2 * (n - i) - 1)
        for k in range(space):
            print("  ", end="")
        for j in range((i * 2) - 1, 0, -2):
            if j != 2 * n - 1:
                print(j, end=" ")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(1, i * 2, 2):
            print(j, end=" ")
        space = (2 * (n - i) - 1)
        for k in range(space):
            print("  ", end="")
        for j in range((i * 2) - 1, 0, -2):
            print(j, end=" ")
        print()


num(5)
print()


# extra
def num(n):
    for i in range(n + 1, 0, -1):
        print((n + 1 - i) * " ", end="")
        for j in range(1, i):
            print(j * 2, end=" ")
        print()


num(5)


# doble butterfly
def num(n):
    for i in range(1, n + 1):
        for j in range(1, i * 2, 2):
            print(j, end=" ")
        space = (2 * (n - i) - 1)
        for k in range(space):
            print("  ", end="")
        for j in range((i * 2) - 1, 0, -2):
            if j != 2 * n - 1:
                print(j, end=" ")
        print(" ", end="")
        for j in range(1, i * 2, 2):
            print(j, end=" ")
        space = (2 * (n - i) - 1)
        for k in range(space):
            print("  ", end="")
        for j in range((i * 2) - 1, 0, -2):
            if j != 2 * n - 1:
                print(j, end=" ")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(1, i * 2, 2):
            print(j, end=" ")
        space = (2 * (n - i) - 1)
        for k in range(space):
            print("  ", end="")
        for j in range((i * 2) - 1, 0, -2):
            print(j, end=" ")
        space = 1
        for t in range(space):
            print(" ", end="")
        for j in range(1, i * 2, 2):
            print(j, end=" ")
        space = (2 * (n - i) - 1)
        for k in range(space):
            print("  ", end="")
        for j in range((i * 2) - 1, 0, -2):
            if j != 2 * n - 1:
                print(j, end=" ")
        print()


num(5)
print()
