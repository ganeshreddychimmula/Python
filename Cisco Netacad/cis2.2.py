#vowel eater code
print("enter  a word ")
u=input()
for i in u:
    i=i.upper()
    if i =="A" or i == "E" or i == "I" or i == "O" or i == "U":
       continue
    print(i,end="")