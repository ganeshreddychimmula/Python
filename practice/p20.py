N = int(input())
N_i = input().split(" ")
N_lab = input().split(" ")
for i in range(N):
    N_i[i] = float(N_i[i])
    N_lab[i] = float(N_lab[i])

def main():
    ppg = 0

    try:
        while True:
            for i in range(N):
                if not N_lab[i] <= 0:
                    N_lab[i] -= N_i[i]
                else:
                    raise Exception
            ppg += 1
    except:
        return ppg


print(main())
#4
#2 5 6 3
#20 40 90 50