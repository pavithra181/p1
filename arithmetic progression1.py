n,a,d=map(int,input().split())
if n>=1 and n<=100000:
	if a>=1 and a<=100000:
		sn=(n*(2*a+((n-1)*d)))/2
		print(sn)
