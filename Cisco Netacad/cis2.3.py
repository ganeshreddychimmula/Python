blocks =int(input("enter number of blocks"))
layerblocks=0#number of blocks in that particular layer
layer=0#layer it is in
for i in range(1,blocks+1):
    layerblocks+=1
    if layerblocks==layer+1:
        layer+=1  #layer value increases only when the layer blocks create a complete layer
        layerblocks=0 #after completion of every layer, layerblocks value resets
        count=0 #used to count blocks that were not able to form a complete layer
    else:
        count+=1
        continue
print("height of pyramid :",layer)
print("number of blocks wasted ",count)