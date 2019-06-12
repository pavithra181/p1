n=input()
k=0
for x in n:
    if(x.isdigit()!=True and x.isalpha()!=True and x.isspace()!=True ):
        k=k+1
print(k)
