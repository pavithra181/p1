n,m=map(int,input().split())
for i in range(n+1,m):
    a=i
    sum=0
    while(i!=0):
        r=i%10
        sum=sum+r*r*r
        i=i//10
    if(a==sum):
        print(a,end=" ")
