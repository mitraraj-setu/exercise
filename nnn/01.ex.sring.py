#1

m = "w3school"
count = 0

for i in m:
    count += 1
print(count)

#2
m = "w3school"
print(m[:2]+m[-2:])


#3
m = "test"
first_t = m.find("t")
second_t = m.find("t")
n = (m[:3]+m[:second_t]+"$")
print(n)


#4
m = "xyz"
print(m[-1]+m[1]+m[0])



#5
m = "w3school"
print(m[:4]+m[-4:].upper())