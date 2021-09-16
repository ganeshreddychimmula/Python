#class vechile:
#    print("hello i am rom class vechile")
#print(type(vechile))
#moving=vechile()
#whole part is called definition while rhs part is called instantiation
#print(type(moving))
#stack - procedural programming
stack = []

def push(val):
    stack.append(val)
    print(stack)


def pop():
    val = stack[-1]
    del stack[-1]
    return stack

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
