#1
S='w3school'
a=len(S)
print(len(S))

#2
S='w3school'
if a<2:
    print("")
else:
    d=S[:2]
    s=S[-2:]
    print(d+s)

#3
A='testtest'
c=A.replace("t","$")
d=c.replace("$","t",1)
print(d)                 

#4
w='xyz'
a=w.replace(w[-1],"x")
b=a.replace("x","z",1)
print(b)

#5
Input = 'w3schoolk'
a=Input[4:]
b=Input[:4]
c=a.upper()
print(b+c)

#