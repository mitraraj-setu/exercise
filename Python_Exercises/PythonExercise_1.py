a = {'a': 10, 'b': 20, 'c': 30}
b = {'a': 5, 'd': 15, 'c': 10}
new_dict = {}

for x in a:
    for y in b:
        if(x == y):
            a[x] = a[x] + b[y]
            new_dict.update({y: a[x]})

        else:
            new_dict.update({x:a[x]})

for y in b:
    if(y in new_dict.keys()):
        pass
    else:
        new_dict.update({y: b[y]})

print(new_dict)