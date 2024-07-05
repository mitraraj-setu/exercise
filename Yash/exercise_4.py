#
# # Import the 'reduce' function from the 'functools' module.
# from functools import reduce
#
# # Define a function 'test' that calculates the LCM (Least Common Multiple) of a list of numbers.
# def test(nums):
#     # Use the 'reduce' function to apply the 'lcm' function cumulatively to the elements of 'nums'.
#     return reduce(lambda x, y: lcm(x, y), nums)
#
# # Define a function 'gcd' that calculates the Greatest Common Divisor (GCD) of two numbers.
# def gcd(a, b):
#     # Use the Euclidean algorithm to find the GCD of 'a' and 'b'.
#     while b:
#         a, b = b, a % b
#     return a
#
# # Define a function 'lcm' that calculates the Least Common Multiple (LCM) of two numbers.
# def lcm(a, b):
#     # Calculate the LCM using the formula: LCM(a, b) = (a * b) / GCD(a, b).
#     return a * b // gcd(a, b)
#
#
#
# l1=[2,3,8]
# q=test(l1)
# l2=[9,7]
# w=test(l2)
# print(w)
# n=100
# Z=[]
# for i in range(1,n):
#     if i % q == 0:
#         Z.append(i)
# print(Z)
# x=[]
# for u in Z:
#     if all(u%r != 0 for r in l2):
#         x.append(u)
# print(x)


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
