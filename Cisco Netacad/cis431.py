#using map example
list1 = [x for x in range(5)]
list2 = list(map(lambda x: 2 ** x, list1))
print(list2)
for x in map(lambda x: x * x, list2):
	print(x, end=' ')
print()


#using ilter example
for x in filter(lambda x: x>0 and x%2==0, list1):
	print(x, end=' ')
