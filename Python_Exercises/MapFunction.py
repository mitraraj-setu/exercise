def func(n):
    letters = ['a', 's', 'f', 'l', 'r']
    if(n in letters):
        return  True

    else:
        return False

sequence = ['s','w', 't', 'a', 'y']

f = filter(func, sequence)

print(list(f))