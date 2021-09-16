class SampleClass:
    def __init__(self, val):
        self.val = val

ob1 = SampleClass(0)
print(ob1.val)
ob2 = SampleClass(2)
ob3 = ob1
ob3.val += 1

print(ob1 is ob2)
print(ob2 is ob3)
print(ob3 is ob1)
print(ob1.val, ob2.val, ob3.val)

str1 = "Mary had a little "
str2 = "Mary had a little lamb"
str1 += "lamb"

print(str1 == str2, str1 is str2)
#these results show that ob1&3(variables) point to same object
#those are two different variables