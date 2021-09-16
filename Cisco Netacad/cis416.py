class Level1:
    var = 100
    def fun(hi):
        return 101

    def doit(hi):
        print("doit from One")

    def doanything(hi):
        hi.doit()

class Level2(Level1):
    var = 200
    def fun(self):
        return 201

    def doit(self):
        print("doit from Two")

class Level3(Level2):
    def doit(self):
        print("doit from Three")

obj = Level3()

print(obj.var, obj.fun())

one = Level1()
two = Level2()
three=Level3()

one.doanything()
two.doanything()
three.doanything()

#result
# 200 201
#doit from One
#doit from Two
#doit from Three