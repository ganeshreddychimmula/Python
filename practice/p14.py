#write a Python program to find the number of divisors of a given integer is even or odd. Go to the editor
def noofd(n):
    global d
    d=[]
    for i in range(n//2,1,-1):
        if n%i==0:
            d.append(i)
    return len(d)
def evenodd(ll):
    if ll==0:
        print("number of divisors are even")
    else :
        print("number of divisors are odd")
try:
    while True:
        number=int(input("enter the number"))
        evenodd(noofd(number))
        print(d)
except Exception as e :
    #print(e)
    pass