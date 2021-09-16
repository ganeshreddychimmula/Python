from os import strerror
import errno
cnt=1
try:
    s=open("H:\sample\sample3.txt","rt")
    ch=s.readline(1)#first  character is read and header is moved to second
    ch=s.readline()
    while ch!="":
        cnt += 1
        print(ch)
        ch=s.readline()
    s.close()
    print("number of lines:",cnt)
except IOError as err:
    print("error occured",strerror(err.errno))

cnt=1
try:
    s=open("H:\sample\sample3.txt","rt")
    lines=s.readlines()#first  character is read and header is moved to second
    for i in lines:
       print(i)
    #while ch!="":
        #cnt += 1
        #print(ch)
        #ch=s.readline()
    s.close()
    print("number of lines:",cnt)
except IOError as err:
    print("error occured",strerror(err.errno))