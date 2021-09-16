#code for array sum

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    summ = 0
    for i in range(ar_count):
        summ = summ + ar[i]
    return summ
ar_count = int(input("enter arraysize"))
ar = list(map(int, input("enter array").rstrip().split()))
z=simpleArraySum(ar)
print(z)