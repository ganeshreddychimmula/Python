#list1 = [1,3,4,5,6]
#list2=list1#diferent lists pointing to same memory location
#list3 = list1[:]#using slice element in python to copy whole list
#list4 =list1[1:3]#2nd and third element
#list1[0] = 2
#print(list1,list2,list3,list4,"\n",id(list1),id(list2),id(list3),id(list4))
#var1=2
#var2=var1
#var1=0
#print(var1,var2,id(var1),id(var2))
#the name of an ordinary variable is the name of its content;
#the name of a list is the name of a memory location where the list is stored.
#print(list1[2:-1])
#print(list1[-1:1])#no error ,just gives an empty list
#list1.clear()
#print(list1)
####program to remove dupicate values from a lis####
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2,9]
b=[]
for i in range(len(myList)):
    for j in range(len(myList)):
        if i in b:
            continue
        elif i!=j:
            if myList[i]==myList[j]:
                b.append(j)
                print(j,"set in b")
b.sort()
print(b)
b.reverse()#to get in descending order so that deleting elements doesnt effect the list
print(b)
for num in b:
    del(myList[num])

print("The list with unique elements only:")
print(myList)