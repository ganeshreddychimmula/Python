#bubblesort
#swap adjacent values in a list

a=[4,3,5,2,566,78,23,5,2,4,5,6,7]

l=len(a)
for j in range(l-1):
    for i in range(l-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    l=l-1
print("sorted array",a) 