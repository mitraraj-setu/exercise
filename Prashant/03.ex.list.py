

#1
list = ["Complete", " sentence", " Complete", " exercise"]
x = 0
for i in list:
    if list.index(i) == x:
        print(i, list.count(i))
    x += 1

print()
#2

str = "Complete sentence Complete exercise"
x = {}
l = str.split()

for i in l:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1
print(x)
#3
# for a, b in x.items():
#     print(a, b)

list = [10, 12, 20, 22]
x = 0
for i in list:
    x = x + i
print(x)

list = [10, 12, 20, 22, 2]
x = list[0]
for i in list:
    if i < x:
        x = i
print(x)
#4




#5
list = ['abc', 'xyz', 'aba', '1221']
s = 0
for i in list:
    if len(i) > 1 and i[0] == i[-1]:
        print(i)
        s = s+1
print(s)



#6
list = [10, 12, 20, 22, 10, 20, 22]
d = []
for i in list:
    if i not in d:
        d.append(i)
print(d)


#7 list1 akhi list sathe 1 to 100 ma koy pn number divaid kari sake and list2  ma tej rakam devaid na karisake teva number
list1 = [2,3,5]
list2 = [8,12]

result = []

for i in list1:           #a condishan bane list sem and ak pn carecter mech thay hoy to loop false thay jashe
    if i in list2:
        print(result)
        exit()

if list1 == list2:         # bane list sem hoy to
    print(result)

elif 0 in list1 or 0 in list2:          #0 bane mathi koy pn list ma jo 0 avshe to loop falsh
    print(result)

elif 1 in list1 or 1 in list2:           #1bane mathi koy pn list ma jo 1 avshe to loop falsh
    print(result)


else:
    for i in range(1, 100):
        if all(i % x == 0 for x in list1):              #all  vapar vathi list na badha eliment sathe chek kar se pachi condishan agad jashe
            if all(i % y != 0 for y in list2):
                result.append(i)

    print(result)



#one line cod uper no
list1 = [2, 4, 5]
list2 = [8, 12]


if any(i in list2 for i in list1) or list1 == list2 or 0 in list1 or 0 in list2 or 1 in list1 or 1 in list2:
    print(result)


result = [i for i in range(1, 1000) if all(i % x == 0 for x in list1) and all(i % y != 0 for y in list2)]
print(result)




#888   index thi list ni values medva mate
thislist = [5, 7,9,1,6,4,3]

x = thislist[1]

print(x)


#9999 index thi list ni values medva mate

class Index:
    def __init__(self):
        self.l3 = {}

    def di(self, l, target):
        for i in l:
            self.l3.update({i: l.index(i)})

        for i, y in self.l3.items():
            if y == target:
                return i

    def ub(self, *add):
        l.extend(add)


l = ["org", "app", "uc"]
x = Index()


