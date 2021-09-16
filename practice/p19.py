#Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.
#Create a function, that takes an integer (radius of the circle) and returns the square area of the square inside the circle.
#by calculation we got side=radius**0.5
def area(n):
    s1=n*(2**0.5)
    s2=n
    return s1*s1
r=int(input("enter the circle radius"))
print("area of incircle:",area(r))