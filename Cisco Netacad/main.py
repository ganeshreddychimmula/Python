#import module
#from sys import path
#for i in range(len(path)):
#  print(path[i],"\n")
#print(__name__)
#path.append("D:\krishna")
#import hi
from sys import path
path.append("H:\python\ciscopackage")
#from extra.iota import funI
#print(funI())
import extra.good.best.sigma  #sigma is the module
from extra.good.best.tau import FunT

print(extra.good.best.sigma.FunS())
print(FunT())