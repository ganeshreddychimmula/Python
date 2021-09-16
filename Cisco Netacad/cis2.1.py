
import time
i=1
count=0
while i:
    if i==8 or i==6:
        i+=1
        continue#when this appears program ignores loop body after this and continues to execute
    if i==10:
        print("f**k this,here i come")
        break
    print("misissippi",i)
    i+=1
    time.sleep(1)
print("haha you're so dead")