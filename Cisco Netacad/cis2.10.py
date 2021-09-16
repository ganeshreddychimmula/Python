
def isYearLeap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
def daysInMonth(year, month):
    mnyear=[31,28,31,30,31,30,31,31,30,31,30,31]
    mlyear=[31,29,31,30,31,30,31,31,30,31,30,31]

    y = isYearLeap(year)
    while month in range(1,13):
        if y:
            return mlyear[month - 1]
        else:
            return mnyear[month - 1]
    else:
        return None

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 13]
testResults = [28, 29, 31, None]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
from platform import platform as plat
print(plat())