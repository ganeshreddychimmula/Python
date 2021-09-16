histream=open("H:\sample\sample.txt",'rt')
ch=histream.read(1)
cnt=0
while ch!="":
    cnt+=1
    print(ch,end="")
    ch=histream.read(1)
histream.close()
print("characters in file:",cnt)
#from os import strerror


