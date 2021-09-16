#try:
#   x=int(input("enter the value of x:"))
#   y=int(input("enter the value of y:"))

 #  try:
   #     print("how are you",x/y )
  # except:
    #    print("exception raised")
#except:
 #  print("exception raised most likely due to value error")
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except ValueError:
    print("You ")
except IndexError:
    print("djdjsj")
except:
    print("Oh dear, something went wrong...")

print("THE END.")