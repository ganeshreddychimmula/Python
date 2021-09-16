#Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers.
from random import choice,sample
import time
x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
#x=[1,2,3,4,5,56,7]
j=True
count=0
while j:
        li=sample(x,3)
        if li[0]+li[1]+li[2]==0:
            print(li)
            break
        count+=1
        if count==100:
            print("there is no such triplet in given set ")
            break
