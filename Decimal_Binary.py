import math
def Decimal_Binary(x):
    print(x)
    if x>=2:
        print("test ")
        while x>=2:
            a="x"
            if x>=2: 
               x==x//2
               y=str(int(math.remainder(x,2)))
               y==str(y)+str(a)
               if x<2:
                   break
                   if x==1:
                       c==str("1")
                       y==str(y)+str(c)
                   elif x==0:
                       c==str("0")
                       y==str(y)+str(c)   
    else:
        if x==1:
            y=str("1")
        elif x==0:
            y=str("0")
    return str(y)[::-1]

x=int(input("give number"))
v=Decimal_Binary(x)
print(v)
