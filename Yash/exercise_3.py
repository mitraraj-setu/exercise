# 1

l = "Complete sentence Complete exercise"
l1 = l.split(" ")     #split return list
print(l1)
l5 = []
for i in l1:
    if i not in l5:
        l5.append(i)
for i in l5:
    print(i, l1.count(i))

# 2
I = [10, 12, 20, 22]
i = 0
for x in I:
    i = i + x
print(i)

# 3
p = [10, 12, 20, 22, 2]
i = p[0]
for x in p:
    x < i
    i = x
print(i)

# 4
I = ['abc', 'xyz', 'aba', '1221']
sum = 0
for x in I:
    if len(x) > 2 and x[0] == x[-1]:
        sum += 1
print(sum)

# 5
I = [10, 12, 20, 22, 10]
b = set(I)
c = list(b)
print(c)

