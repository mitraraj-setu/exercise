# Empty Student Dictionary
stud_dict = {}

# N = Number of students
N = int(input("Enter the nunbers of students: "))

for i in range(N):

    # Student Marks Dictionary
    marks = {"Maths": 0, "Physics": 0, "Chemistry": 0}

    print("Enter the name of student " + str(i+1) + ": ")
    name = input()

    print("Enter the marks for Maths, Physics and Chemistry: ")
    for x in marks:
        num = float(input())
        # scores = float(num)
        marks[x] = num

    stud_dict[name] = marks

print("The names and marks of students are:")
print(stud_dict)

# Percentage
selected_stud = input("Enter the name of the student you want the percentage marks of: ")

sum = 0
for x in stud_dict[selected_stud].values():
    sum = sum + x

percentage1 = sum/3
percentage = format(percentage1, '.2f')
print("The percentage marks of " + selected_stud + " are " +percentage)