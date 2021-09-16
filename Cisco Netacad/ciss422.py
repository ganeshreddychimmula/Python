try:
    i =int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())
    print(e.args)

try:
    #print(1/0)
    raise ZeroDivisionError("saregama")
except Exception as d:
    print(d)
    print(d.__str__())
    print(d.args)