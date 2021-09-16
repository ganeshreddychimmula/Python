class stack:
    def __init__(self):
        self.__stacklist=[]
    def push(self,val):
        self.__stacklist.append(val)
    def pop(self):
        val=self.__stacklist[-1]
        del self.__stacklist[-1]
        return val
class stackadd(stack): #subclass of stack
    def __init__(self):
        stack.__init__(self)
        self.__sum=0
    def push(self,val): #push method overriden
        self.__sum+=val
        stack.push(self,val)
    def pop(self):     #pop overriden
        val=stack.pop(self)
        self.__sum-=val
        return val
    def getsum(self):
        return self.__sum
o1=stackadd()
count=0
for i in range(5):
    count+=1
    y=count+i
    print("y=",y)
    o1.push(y)
print("sum=",o1.getsum())
for i in range(5):
    print(o1.pop(),"got popped")

print("sum=",o1.getsum())