# Dimensions of the cuboid

x = int(input("Enter the length of cuboid:"))
y = int(input("Enter the breadth of cuboid:"))
z = int(input("Enter the height of cuboid:"))
n = int(input("Enter the sum to be excluded:"))

# x=1
# y=1
# z=1
# n=2

# Using nested for loops

# coordinates_list = []
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if (i+j+k != n):
#                 coordinates_list.append([i,j,k])

# Using List Comprehension
coordinates_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]

print("The remaining coordinates not having sum " +str(n)+" is",coordinates_list)