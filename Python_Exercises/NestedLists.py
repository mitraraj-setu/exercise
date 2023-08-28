# Number of students
N = int(input("Enter the number of students: "))

while (N<2 or N>5):
    print("Invalid number of students. Enter students from 2 to 5. :")
    N = int(input())

    if(N<2 or N>5):
        continue
    else:
        break

# Empty List
Student_Physics_List = [[] for i in range(N)]

# Creating Nested List
for i in range(N):

    print("Enter the name of student ",(i+1), ":")
    student_name = input()
    physics_marks = float(input("Enter the physics marks: "))

    Student_Physics_List[i].append(student_name)
    Student_Physics_List[i].append(physics_marks)

# Sorting and printing Nested List
Student_Physics_List.sort()
print("The students and the marks that you entered are:")
print(Student_Physics_List)

# Creating a separate marks list
marks = sorted([Student_Physics_List[i][1] for i in range(N)], reverse=True)

# Logic for finding the second last scoring students
temp = 0
if(N == 2):
    temp = marks[1]

else:
    for i in range(len(marks)-1):
        if(marks[i+1] < marks[i]):
            if(marks[i+2] <= marks[i+1]):
                temp = marks[i+1]
                break
        else:
            continue

Second_Last = [Student_Physics_List[i] for i in range(N) if Student_Physics_List[i][1] == temp]

Sorted_Second_Last = sorted([k for k,l in Second_Last])

print("The Second-last standing students are:")
for i in Sorted_Second_Last:
    print(i)