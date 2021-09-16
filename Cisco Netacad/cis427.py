class Fib:
    def __init__(self, nb):
        print("__init__")
        self.__n=nb
        self.__i=0
        self.__p1=0
        self.__p2=1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i==1:
            return 0
        if self.__i==2:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

for i in Fib(10):
    print(i)