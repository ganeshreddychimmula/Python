arr = [2,6,1,9,4,5,3]

lis = list(filter(lambda x : x+1 in arr, arr))
print(len(lis)+1)