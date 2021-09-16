#print(print("print(\"Hello!\")"))
#print(print())
#print("Programming","Essentials","in",sep="***",end="...")
#print("python")
#print(3e8)
#print(0.0000000000000000000002mn
blocks=int(input("enter total no. of blocks \n"))
layerblocks=0
layer=0
for i in range(1,blocks+1):
   layerblocks+=1
   if layerblocks==layer+1:
       layer+=1
       layerblocks=0
print("total number of layers possible are ",layer,"and remaining incomplete blocks are",layerblocks)