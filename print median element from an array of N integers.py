a=int(input())
a1=list(map(int,input().split()))
b=len(a1)
a1.sort()
c=a1[int(b/2)]
print(c)
