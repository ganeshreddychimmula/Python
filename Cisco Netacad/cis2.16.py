#dct={}
#dct[0]=1
#dct[1]=2
#print(dct)
class A:
    def __init__(self,v=2):
        self.v=v
    def set(self,v=1):
        self.v+=v
        return self.v
a=A()
b=a
b.set()
print(a.v)
print(len("\\\\"))
d=open('H:\sample\\sample.txt','rt')
print(d.readlines())
t=(1,)
t=t[0]+t[0]
for r in range(0):
    print(r)
str1="jhej"
str2=str1[:]
print(id(str1),id(str2))
str="dhdh"
#str[2]="s"
print(True and True )
x="""
"""
print(len(x))
print([i for i in range(0)])
class A:
    __a=0
b=A()
print(9 if 2%2==0 else 3)