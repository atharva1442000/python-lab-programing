x=int(input("enter a number="))
a=x%10
b=a **3
c=x//10
d=c%10
e=d **3
f=c//10
g=f **3
h=g+e+b
if x==h:
    print(x,"is a armstrong number")
else:
    print(x,"is not a armstrong number.")