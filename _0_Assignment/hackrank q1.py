n=int(input())
a,b=0,3
for i in range(1,n+1):
    for j in range(1,i+1):
        a=a+2
        if(i==1):b=3
        else:b=b+4
        re=a*b
        print("%.5d"%(re),end=" ")
    print()