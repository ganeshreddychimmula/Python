#number of increasing layers possible

n=int(input("enter number of blocks"))
l=0  #layers
s=n
while s>l:
    l=l+1
    s=s-l
print("number of possible layers",l)

