#Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

def gcd(x,y):
    x1=[]
    y1=[]
    gcd=1
    for i in range(2,x):
        if x%i==0:
            x1.append(i)

    for i in range(2,y):
        if y%i==0:
            y1.append(i)
    for i in x1:
        if i in y1:
            gcd=i
    return gcd
print(gcd(int(input("enter 1")),int(input("enter 2"))))#336,360 gives 24