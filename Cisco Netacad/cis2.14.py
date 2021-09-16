#tic-tac-toe
status=0
from random import randrange
gamestatus=0
ttboard = [[i for i in range(3)] for j in range(3)] #create board
count = 0

for i in range(3):
    print(ttboard[i])

theboard={}#create dictionary
for i in range(1,10):
    theboard[i]=i
print(theboard)

def displayboard():
    val=0
    for i in ttboard:
        for j in range(3):
            val += 1
            i[j] = theboard[val]
    for i in range(3):
        for j in range(3):
           print(ttboard[i][j],end="     ")
        print("\n")

def emptysquares():
   emptyboxes=[]#list
   for i in range(1,10):
       if theboard[i] in range(1,10):
           emptyboxes.append(i)
  # print("emptyboxes:",emptyboxes)#code runs even print this line return is the only value that returns to function call
   return emptyboxes




#if status even its players turn
#if status is odd its computers turn
def computerturn():
    global status
    while True:

       x=randrange(1,10)
       if x in emptysquares():
           break
    theboard[x]="x"
    displayboard()
    status=0

def userturn():
    global status
    v = emptysquares()
    while True:
        y=int(input("enter a number in range 1-9"))
        if y in v:
            break
    theboard[y]="o"
    displayboard()
    status =1

winningsets=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

def win():
    for k in winningsets:
        p = []
        for j in range(3):
            p.append(theboard[k[j]])
        if p[0] == p[1] == p[2]:
            if p[0] == "o":
                print("you have won")
            else:
                print("you have lost")
            return 1
            break
    else:
        print("continue playing games")
    return 0
def draw():
    p=emptysquares()
    if p==[]:
       print("match is drawn")

       return 2
    else:
       return 0

#computers 1st turn
theboard[5]="x"
print(displayboard())
#gamecode
while gamestatus==0:
    if status%2==0:
        userturn()
    else:
        computerturn()
    m = win()
    n = draw()
    gamestatus = m or n
print(gamestatus)
