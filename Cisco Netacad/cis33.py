def fun():
    try:
        #raise ZeroDivisionError#works
        raise ArithmeticError
    except ArithmeticError:
      print("Oooppsss...")
      raise

try:
    fun()
#except ArithmeticError:
except ZeroDivisionError:
    print("awwh,i did it again")
except:
    print("i guess arthemetic error cannot be handled by ZeroDivisionError,while,viceversa it is true")


print("THE END.")