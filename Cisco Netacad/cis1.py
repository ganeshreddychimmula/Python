# print(print(print("Hello!")))
#print("Welcome to Python Essentials!")
#print("THIS IS SANDBOX \"MODE.")
#print("Programming","Essentials","in",sep="***",end="...")
#print("Python")
#print(3e8)
#print(0.0000000000000000000001)
#hi=1
#print(hi)
#var = 1
#print(var)
#var += 1
#print(var)
#Round=round(3.676767575443,3)
#print(Round)
#num=3
#print(float(num))
#print("Tell me anything...")
#anything = int(input())
#print("Hmm...", anything, "... Really?")
#something = input("say something")
#print(something)
#anything = input("Enter a number: ")#input() function result is a string
#something = anything ** 2.0
#print(anything, "to the power of 2 is", something)
#print(20.12e8)
#x, y, z = 5, 10, 8
#x, y, z = z, y, x used for swapping variables
#print(x,y,z)
#while True:
#    print("i'm stuck")
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# read the first number
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution
while number:
    # check if the number is odd
    if number % 2 == 1:
        # increase the odd_numbers counter
        odd_numbers += 1
    else:
        # increase the even_numbers counter
        even_numbers += 1
    # read the next number
    number = int(input("Enter a number or type 0 to stop: "))

# print results
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)