#staircase
   #
  ##
 ###
####
#problem

def staircase(num):
    ar=[" "]*n
    for i in range(1,n+1):
       ar[-i]='#'
       print(''.join(ar))


n=int(input("enter the height : "))
staircase(n)