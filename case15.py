A1,B=map(int,input().split())

for i in range(A1+1,B):

    if(i%2==0 and i!=B-1):

        print(i,end=" ")

    elif(i%2==0 and i==B-1):

        print(i)
