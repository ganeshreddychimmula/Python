class star:
    def __init__(self,name,galaxy):
        self.name=name
        self.galaxy=galaxy
    def __str__(self):
        return self.name +" in "+ self.galaxy
planet=star("saturn","milkyway")
print(star.__name__)
print(star.__module__)
print(planet.__module__)
print(type(planet).__name__)
print(isinstance(planet,star))

#print(planet.__name__)#error because its not object property to access
print(planet)