def plus(a,b):
    c=a+b
    if c>=100:
        return c
    a,b=b,c
    plus(a,b)

print(plus(10,20))