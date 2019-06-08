n,m=map(int,input().split())
for i in range(n+1,m): 
  c=0
  for j in range(1,m):
    if(i%j==0):
      c=c+1
  if(c==2):
    print(i,end=" ")
