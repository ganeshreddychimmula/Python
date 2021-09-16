#. Write a Python program to reverse the digits of a given number and add it to the original,
# If the sum is not a palindrome repeat this procedure
def pal(k):
    global sum
    sum=0
    ok=k
    while k>0:
        n=k%10
        sum=sum*10+n
        k=k//10
    if ok==sum:
        return True
    else:
        return False
def fun(n):
    snum=n
    while not pal(snum):
        snum=n+sum
    else :
        return snum
number=int(input("enter the number"))
print(fun(number))