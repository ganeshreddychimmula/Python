text=input("enter the string")
ceaser=""
x=int(input("enter the shift value"))
if x not in range(1,26):
    print("enter the correct value")
for i in text:
    if not i.isalnum():
        ceaser+=i
        continue
    y=ord(i)
    if y in range(65,91):
        if y+x>90:
            y=64+(x+y-90)
        else:
            y=y+x
    elif y in range(97,123):
        if y+x>122:
            y=96+(x+y-122)
        else:
            y=y+x
    elif y in range(48,58):
        y=y
    ceaser+=chr(y)
print(ceaser)