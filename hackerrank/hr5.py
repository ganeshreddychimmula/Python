#Given a square matrix, calculate the absolute difference between the sums of its diagonals.

#For example, the square matrix  is shown below:

#1 2 3
#4 5 6
#9 8 9
#The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .
#Function description
#Complete the  function in the editor below.
#diagonalDifference takes the following parameter:

#int arr[n][m]: an array of integers
#Return : int: the absolute diagonal difference
#sample input:
####3
#11 2 4
#4 5 6
#10 8 -12

def diag_diff(arr):
    sum1=0
    sum2=0
    for i in range(n):
        sum1+=arr[i][i]
        sum2+=arr[i][n-1-i]
    return abs(sum1-sum2)

n=int(input("entyer the matrix height : "))
a=[]
for i in range(n):
    a.append(list(map(int,input("enter next row : ").strip().split())))
print(diag_diff(a))
