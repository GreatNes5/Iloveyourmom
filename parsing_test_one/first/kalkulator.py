from math import *
a=int(input())
b=int(input())
c=int(input())
d=b*b-4*a*c
if d<0:
    print("Корней нет")
elif d == 0:
    x=((-b-sqrt(d))/(2*a))
    print(x)
elif d > 0:
    x1=((-b-sqrt(d))/2*a)
    x2=((-b+sqrt(d))/2*a)
    print(max(x1,x2))
    print(min(x1,x2))
