def power(a,b):
    if b == 1:
        return a
    else:
        return a*(power(a,b-1))


a = int(input('Enter a'))
b = int(input('Enter b'))
s=power(a,b)
print(s)
