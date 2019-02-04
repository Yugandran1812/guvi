num=input()
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if temp==num:
    print("yes")
else:
    print("no")    
    
        
