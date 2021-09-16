#EMPTY = "-"
##ROOK = "ROOK"
#board = [[EMPTY for i in range(8)] for j in range(8)]
#board[0][0] = ROOK
#board[0][7] = ROOK
#board[7][0] = ROOK
#board[7][7] = ROOK
#for k in range(8):
#  print(board[k])
#i=[[0,1,2,3] for j in range(2)]
#print(i[2][0])
#def boringFunction():
#    return 123
#print(boringFunction())

def isYearLeap(year):
    if year%4==0 and year%100!=0:
        return True
    elif year%400==0:
        return True
    else:
        return False
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")