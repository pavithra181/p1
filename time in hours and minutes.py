minutes=int(input())
a=minutes
if minutes>0:
	minutes=a%60
	hours=a//60
	print(hours,minutes)
