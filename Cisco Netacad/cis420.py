#diamond problem in multipleinheritance
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(A, B):
    pass

d = D()
#python doesnt allowthis type of hierarchies
# #typeError: Cannot create a consistent method resolutionorder (MRO) for bases A, B