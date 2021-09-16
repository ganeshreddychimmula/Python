#encapsulation
class Stack:
    def __init__(self):
        self.stack1 = [] #is public can be accesed from outside
        self.__stack2=[]#we have placed two underscores before it which makes it private and can't be accesed rom outside
stackObject = Stack()
print(len(stackObject.__stacklist),len(stackObject.__stacklist))

