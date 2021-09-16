c0=int(input("enter a non zero positive number"))
count=-1
while c0>0:
    if c0==1:
        count+=1
        break

    elif   c0%2==0:
        c0=c0//2
        count+=1
    elif c0%2==1: #not required you can use else
        c0=3*c0 + 1
        count+=1
    print(c0)
print("steps=",count)


