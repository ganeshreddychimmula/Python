class ExampleClass:
    varia = 1
    def __init__(self, val):
        self.varia = val
        ExampleClass.varia = val+1


print(ExampleClass.__dict__)
exampleObject = ExampleClass(2)

print(ExampleClass.__dict__)
print(exampleObject.__dict__)
print(ExampleClass.varia)
print(exampleObject.varia)
