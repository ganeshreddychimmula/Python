#You are in charge of the cake for a child's birthday.
# You have decided the cake will have one candle for each year of their total age.
# They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

#Example#####
#candles=[4,4,1,3]
#The maximum height candles are  units high. There are  of them, so return .
#sample input:
#4
#3 2 1 3
#program :

def bccandles(candles):
    maxi=max(candles)
    maxi_count=0
    for i in candles:
        if i==maxi:
            maxi_count+=1
    return maxi_count


c_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
print(bccandles(candles))