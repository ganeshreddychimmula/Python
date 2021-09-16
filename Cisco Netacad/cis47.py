#when instance variable names are set private
class class1:
    counterone=0
    __countertwo=0
    def __init__(self, val = 1):
        self.__first = val
        class1.counterone+=1
        class1.__countertwo+=1


    def setsecond(self, val = 2):
        self.__second = val

o1=class1()
o2=class1(2)
o3=class1(3)

o2.setsecond(4)
o3.setsecond(5)
o3._class1__second=6
o3.three=4

print(o1.__dict__,o1.counterone,o1._class1__countertwo)
print(o2.__dict__,o2.counterone,o2._class1__countertwo)
print(o3.__dict__,o3.counterone,o3._class1__countertwo)

print(o1.__module__)
print(class1.__module__)
print(o1.__weakref__)
print(o1.__weakref__)

print(hasattr(o1,'__module__'))
print(hasattr(o1,'_class1__second'))
print(hasattr(o2,'_class1__second'))
print(hasattr(o1,'__dict__'))
print(hasattr(o1,'__weakref__'))
print(hasattr(o1,'__module__'))

print(hasattr(class1,'__module__'))
print(hasattr(class1,'_class1__second'))
print(hasattr(class1,'_class1__second'))
print(hasattr(class1,'__dict__'))
print(hasattr(class1,'__weakref__'))
print(hasattr(class1,'__module__'))
#for i in class1.__dict__.keys():
#    print(i,":",class1.__dict__[i])