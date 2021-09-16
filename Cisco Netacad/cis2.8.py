#program to remove duplicate values
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
myList.sort()
print(myList)
a=[]
for i in range(len(myList)-1):
    print(i)
    if myList[i]==myList[i+1]:
       a.insert(0,i+1)#indices in descendin order
for j in a:
  del(myList[j])
  print(j,"got deleted")

print(myList)