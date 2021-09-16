'''
input:
5
1 2 1 3 2
3 2
output
2
'''
def ways(n,arr,d,len):
    nways=0
    for i in range(n-len+1):
        sum=0
        for j in range(len):
            sum+=arr[i+j]
        if sum==d:
            nways+=1
    return nways




n=int(input().strip())
choc=list(map(int,input().strip().split()))
datemonth=list(map(int,input().strip().split()))#day month
#print(n,choc,datemonth)
print(ways(n,choc,datemonth[0],datemonth[1]))

