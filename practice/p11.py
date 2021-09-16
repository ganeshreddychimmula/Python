# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other
li=[]
print("enter five numbers")
for i in range(5):
    y=int(input(""))
    li.append(y)
z=True
for i in li:
    count=0
    for j in li:
        if i==j:
            count+=1
    if count>1:
        z=False
        k=i
        break
if z:
    print("each value is unique")
else :
    print(k,"ocurred",count,"times")
