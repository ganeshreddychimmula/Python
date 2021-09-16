def getTotalX(a, b):
    if a[-1]>b[0]:
        return 0
    sol=[]
    for j in range(1,m+1):
        temp=[]
        k=1
        while ((a[-j] * k) <=b[0]):
            temp.append(a[-j] * k)
            k+=1
        print(temp)
        if sol==[]:
              sol=temp[:]
              continue
        else:
            tempset=set(temp)
            solset=set(sol)
            finalset=solset.intersection(tempset)
            sol=list(finalset)
            sol.sort()
    print(sol)
    finalsol=[]
    for i in sol:
        for j in range(n):
            if b[j]%i!=0:
                break
        if j==n-1:
            finalsol.append(i)
    return len(finalsol)
first_multiple_input = input().rstrip().split()
m = int(first_multiple_input[0])
n = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))
total = getTotalX(arr, brr)
print(total)


