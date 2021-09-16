T = int(input())

def main():
    N = int(input())
    tgr = input().strip().split(" ")
    tas = input().strip().split(" ")
    for i in range(N):
       tgr[i] = int(tgr[i])
       tas[i] = int(tas[i])
    count = 0
    tgr1 = []
    tas1 = []
    while tgr!=[]:
        tgr.sort()
        tas.sort()
        if tgr[-1] <= tas[-1]:
            tgr[0], tgr[-1] = tgr[-1], tgr[0]
        tgr1.insert(0, tgr[-1])
        tas1.insert(0, tas[-1])
        del tas[-1]
        del tgr[-1]
    #print(tgr1)
    for i in range(N):
        if tgr1[i] > tas1[i]:
            count+= 1
    return count
for i in range(T):
    print(main())

#1
#10
#3 6 7 5 3 5 6 2 9 1
#2 7 0 9 3 6 0 6 2 6