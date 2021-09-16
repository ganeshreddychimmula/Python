from random import *
from platform import *
import math
#print(dir(math))

print(platform(),machine(),version(),sep="||")
print(math.__name__)
import sys
for i in sys.path:
    print(i,end="\n   ")
class hello :
    __y=100000

h=hello()
print(h._hello__y)