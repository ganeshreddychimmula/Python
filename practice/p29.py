'''
practice
'''
'''
input:
apple59red
apple5red
'''
index = -1
inp = list(input())
l = len(inp)
for i in range(l):
    if ord(inp[i])<=57 and ord(inp[i])>=48:
        v = int(inp[i])
        if v == l-1:
            index = i
            break
inp = "".join(inp[:index]) + "".join(inp[index+1:])
print(inp)
