lst = [1 if x % 2 == 0 else 0 for x in range(10)]#list comprehension example
genr = (1 if x % 2 == 0 else 0 for x in range(10))#generator

for v in lst:
    print(v, end=" ")
print()

for v in genr:
    print(v, end=" ")
#print(len(genr))