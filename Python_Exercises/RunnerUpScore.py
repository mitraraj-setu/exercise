# Number of participants
num = int(input("Enter the number of participants:"))

if (num < 2 and num > 10):
    num = int(input("Invalid number! Enter number of participants from 2 to 10"))

score_list = []
for i in range(num):
    score = int(input("Enter the scores of participant " + str(i+1)+": "))
    score_list.append(score)

print("The scores that you entered are:", score_list)

# Sorting and Reversing the Score List
score_list.sort()
score_list.reverse()

# Two different conditions for number of participants equal to 2 or more than 2
runner_up = 0
num = len(score_list)

for i in range(num):

    if(num == 2):
        if(score_list[0] > score_list[1]):
            runner_up = score_list[1]
        else:
            print("You have entered same scores for two participants. Hence, there is no runner-up score.")
            runner_up = None
            break

    elif(score_list[i] > score_list[i+1]):
        if(score_list[i+1] >= score_list[i+2]):
            runner_up = score_list[i+1]
            break

    else:
        continue

print("The runner-up score is:", runner_up)