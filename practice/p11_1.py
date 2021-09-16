# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other
li=[]
print("enter five numbers")
for i in range(5):
    y=int(input(""))
    li.append(y)

li.sort()
for i in range(0,len(li)-1):
    count = 0
    if li[i]==li[i+1]:
        count=+1
    if count>0:
        print(li[i], "is repeated",count,"times")
if count==0:
    print("every digit is unique")

