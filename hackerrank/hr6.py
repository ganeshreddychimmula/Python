##Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with  places after the decimal.

#Note: This challenge introduces precision problems.
# The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
#Example
#There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

#0.400000
#0.400000
#0.200000
#Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal.
# The function should not return a value.

#Input Format
#The first line contains an integer, , the size of the array.
#The second line contains  space-separated integers that describe .###

#program  :

#input:
# 6
#-4 3 -9 0 4 1



def plusminus(ar):
    result=[0,0,0]
    for i in range(n):
        if ar[i]>0:
            result[0]+=1
        elif ar[i]<0:
            result[1]+=1
        else :
            result[2]+=1
    for i in range(3):
        print('{:.6f}'.format(result[i]/n))


n=int(input("size of the array : "))
arr=list(map(int,input("enter array : ").strip().split()))
plusminus(arr)

print("{:.2f}".format(3.1415926))
print("{:0>2d}".format(3))
print("{:0<5d}".format(3))
print("{:.3%}".format(0.25))