#u = "Python"
#for i in u:
#    print(i, end="*")
#hi=[1,'a','b',"abba brother",[2,3,4,5]]
#hi.append(8-1)
#print(len(hi),hi)
#hi=[1,2,3,4,5]
#myList = [10, 1, 8, 3, 5]
#length = len(myList)

#for i in range(length // 2):#if length is odd middle element is ignored,else all are swaped in even condition
#    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

#del list #deletes the list itself
#print(myList)
beatles=[]
print("Step 1:", beatles)

beatles.append("john lennon")
beatles.append("paul mccartney")
beatles.append("george harrison")
print("Step 2:", beatles)

for i in range(2):
   y=input("enter the names")
   beatles.append(y)
print("Step 3:", beatles)

del(beatles[3:5])#or use beatles.remove("stu sutcliffe")
print("Step 4:", beatles)

beatles.insert(0,"ringostar")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

