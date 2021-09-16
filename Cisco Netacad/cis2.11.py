#CODE BEGINS HERE
#def bmi(weight, height):
 #   if height < 1.0 or height > 2.5 or \
 #           weight < 20 or weight > 200:
 #       return None

#    return weight / height ** 2
#print(bmi(352.5, 1.65))
#CODE ENDS HERE
def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def isItRightTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(isItRightTriangle(5, 3, 4))
print(isItRightTriangle(2, 4,3 ))
