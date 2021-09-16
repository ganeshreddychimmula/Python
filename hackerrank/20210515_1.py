'''sample input
9
10 5 20 20 4 5 2 25 1
expected output
2 4
'''
def review(n,arr):
    min=max=arr[0]
    #print(min,max)
    review_arr=[0,0]
    for i in range(1,n):
        if arr[i]<min:
            min=arr[i]
            review_arr[1]+=1
        elif arr[i]>max:
            max=arr[i]
            review_arr[0]+=1
    result=" ".join(map(str,review_arr))
    print(result)
    #return result

n=int(input("number of values").strip())
scores=list(map(int,input().strip().split()))#map() excutes eah iterable with specified function and then returns
review(n,scores)
#print(review(n,scores));