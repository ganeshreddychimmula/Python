n=int(input("enter a number"))
sum=0
for i in range(3):
  p=n
  for j in range(i):
      p=p*10+n
  sum+=p
print(sum)
print(n+(n+n*10)+(n+n*10+n*100))