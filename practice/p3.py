# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those number
y=input("input some coma seperated numbers")
l=y.split(",")
t=tuple(l)
print("list,tuple:",l,t)