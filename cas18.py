b,c=map(int,input().split())
for ab in range(b,c):
    sum=0
    x=ab
    while(x>0):
        y=x%10
        sum+=y**3
        x//=10
        if(ab==sum):
            print(sum,end='')
