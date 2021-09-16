T=int(input())
class hello:
    N=0
    t22=[]
    t11=[]
    def __init__(self,n,t1,t2):
        self.t1=[int(i) for i in t1.strip().split(" ")]
        self.t2=[int(i) for i in t2.strip().split(" ")]
        self.N=n
        self.t22=self.t2[:]
    def flist(self):
        while len(self.t1)>0:
            self.t1.sort()
            self.t2.sort()
            #self.t1[-1],self.t1[0]=self.t1[0],self.t1[-1] if self.t1[-1]<self.t2[-1] else  t22=0 #format not correct
            if self.t1[-1] <= self.t2[-1]:
                self.t1[0], self.t1[-1] = self.t1[-1],self.t1[0]
            y=self.t1[-1]
            del self.t1[-1]
            del self.t2[-1]
            self.t11.insert(0,y)
            print(self.t11)
            #yield y
class final:
    #t11=[]
    count=0
    def __init__(self,n,t1,t2):
        self.obj = hello(n,t1,t1)
    def score(self):
        #for i in self.obj.flist():
         #   final.t11.insert(0,i)
        print(self.obj.t11,self.obj.t22)
        self.obj.t22.sort()
        for i in range(self.obj.N):
            if self.obj.t11[i] > self.obj.t22[i]:
                self.count+=1
        return self.count-1

for i in range (T):
    objj=final(int(input()),input(),input())
    print(objj.score())


#hi=hello(3,"1 2 3 4 "," 5 6 7 8 9 ")
#print(hi.t1,hi.t2)
#1
#10
#(3 6 7 5 3 5 6 2 9 1  )
#(2 7 0 9 3 6 0 6 2 6  )

#[3, 5, 5, 6, 6, 3, 2, 7, 9, 1]
