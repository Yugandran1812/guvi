ab=int(input())
sum=0
x=ab
while(x>0):
    y=x%10
    sum+=y**3
    x//=10
   # print(x)
if(ab==sum):
    print('yes')
else:
    print('no')
