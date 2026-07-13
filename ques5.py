def greatest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=c:
        return b
    else:
        return c
x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=int(input("enter third number:"))
print("greatest number=",greatest(x,y,z))
