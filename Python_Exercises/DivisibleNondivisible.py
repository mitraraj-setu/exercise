div = [8,4]
nondiv = [20]

inter_list = []
final_list = []
for i in range(1,10001):
    temp = 0
    for j in div:
        if i%j == 0:
            temp += 1
    if temp == len(div):
        inter_list.append(i)

for i in inter_list:
    for j in range(len(nondiv)):
        if i%nondiv[j] != 0:
            if j+1 == len(nondiv):
                final_list.append(i)
        else:
            break
print(final_list)

# data = [i for i in range(1,10001) if all(i % j == 0 for j in div) and all(i % k != 0 for k in nondiv)]
# print(data)