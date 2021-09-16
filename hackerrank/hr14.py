#!/bin/python3

from math import floor


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (x1>x2 and v1>v2) or (x1<x2 and v1<v2):
        print("NO")
        return

    if v2==v1 :
        print("NO")
        return
    elif x1==x2 and v2!=v1:
        print("NO")
        return
    val = (x1 - x2) / (v2 - v1)
    floorval = floor(val)
    if val>=0 and val==floorval:
        print("YES")
        return
    else :
        print("NO")

i = input().split()
x1 = int(i[0])
v1 = int(i[1])
x2 = int(i[2])
v2 = int(i[3])

kangaroo(x1, v1, x2, v2)
