#bigsorting
# Consider an array of numeric strings where each string is a positive number with anywhere from 1  to 10**6 digits.
# Sort the array's elements in non-decreasing, or ascending order of their integer values and return the sorted array.
#Input Format
#The first line contains an integer, , denoting the number of strings in .
#Each of the  subsequent lines contains an integer string .
#input:
#6
#31415926535897932384626433832795
#1
#3
#10
#3
#5
#program1(selectionsort):

def arraysort(arr):
    result = []
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
        print(arr[i])

n=int(input("number of integers to compare"))
in_array=[int(input().strip()) for i in range(n)]
arraysort(in_array)