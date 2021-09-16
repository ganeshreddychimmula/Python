#stack using object oriented approach
class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)
        #print(self.__stackList)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val
        #print(self.__stackList)
        #return val
o1=Stack()
o1.push(1)
o1.push(2)
o1.push(3)
o1.pop()
o1.pop()
print(o1.pop())
stackObject1 = Stack()
stackObject2 = Stack()

stackObject1.push(3)
stackObject2.push(stackObject1.pop())

print(stackObject2.pop())