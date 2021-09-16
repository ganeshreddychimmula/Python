#read apples and oranges
def count(ad,od):
    applecount,orangecount=0,0
    for i in range(m):
        if a+ad[i]>=s and a+ad[i]<=t:
            applecount+=1
    for i in range(n):
        if b+od[i]>=s and b+od[i]<=t:
            orangecount+=1
    print(applecount)
    print(orangecount)



x=[]
x=list(map(int,input().strip().split()))
s=x[0]
t=x[1]
x=list(map(int,input().strip().split()))
a=x[0]
b=x[1]
x=list(map(int,input().strip().split()))
m=x[0]
n=x[1]
apple=list(map(int,input().strip().split()))
orange=list(map(int,input().strip().split()))
count(apple,orange)