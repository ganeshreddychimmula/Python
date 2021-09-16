class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass

obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)
print(Classy.__name__)
print(type(obj).__name__)

#result
#{'var': 2}
# {'__module__': '__main__', 'varia': 1, '__init__': <function Classy.__init__ at 0x031DD850>, 'method': <function Classy.method at 0x031DD808>, '_Classy__hidden': <function Classy.__hidden at 0x031DD7C0>, '__dict__': <attribute '__dict__' of 'Classy' objects>, '__weakref__': <attribute '__weakref__' of 'Classy' objects>, '__doc__': None}
