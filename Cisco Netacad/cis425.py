#usrdefined exception
class MyZeroDivisionError(ZeroDivisionError):
	pass

def doTheDivision(mine):
	if mine:
		raise MyZeroDivisionError("some worse news")
	else:
		raise ZeroDivisionError("some bad news")

for mode in [False, True]:
	try:
		doTheDivision(mode)
	except Exception:
		print('Division by zero')


for mode in [False, True]:
	try:
		doTheDivision(mode)
	except MyZeroDivisionError:
		print('My division by zero')
	except ZeroDivisionError:
		print('Original division by zero')


#result
#Division by zero #false is passed  ZeroDivisionError object is raised
#Division by zero  #true is passed   MyZeroDivisionError is raised
#Original division by zero  #false is passed  ZeroDivisionError object is raised
#My division by zero        #true is passed   MyZeroDivisionError is raised