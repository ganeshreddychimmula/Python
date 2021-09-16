'''
Fibonacci numbers
'''
def fibonaccisumlastdigit(n):
        print("0 1",end=" ")
        sum=1
        a = 0
        b = 1
        fib = 1
        for i in range(1,n):
            fib = (a+b)
            sum += fib
            a = b
            b = fib
            print(sum%10,"->%d]"%(i),end=" ")
n = int(input())
fibonaccisumlastdigit(n)