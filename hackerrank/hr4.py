#In this challenge, you are required to calculate and print the sum of the elements in an array,
# keeping in mind that some of those integers may be quite large.
#Function Description:
#Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.
#aVeryBigSum has the following parameter(s):
#int ar[n]: an array of integers .
#Return
#long: the sum of all array elements
#sample input:
#5
#1000000001 1000000002 1000000003 1000000004 1000000005

#program:

def arr_sum(array):
    sum=0
    for i in range(ar_size):
        sum+=array[i]
    return sum



ar_size=int(input("enter size"))
ar = list(map(int,input("enter the input array string:").strip().split()))
print(arr_sum(ar))