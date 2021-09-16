#Write a Python program to compute the summation of the absolute difference of all distinct pairs in an given array (non-decreasing order)
x=[1,2,3,4,5,6,7,8,9]
def sumofabdiff(list):
    result=0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            result+=abs(i-j)
    return result
print(sumofabdiff(x))
