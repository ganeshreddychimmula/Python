####Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then pint the respective minimum and maximum values as a single line of two space-separated long integers.###
#input:
#1 2 3 4 5
#expected output: 10 14

#progarm :
def miniMaxSum(arr):
    sum=0
    for i in arr:
        sum+=i
    sum_arr=[sum-i for i in arr]
    result=[min(sum_arr),max(sum_arr)]
    print(" ".join(map(str,result)))



arr = list(map(int, input("enter string conataining values : ").rstrip().split()))
miniMaxSum(arr)
