length1=int(input())
value1=[int(x1) for x1 in input().split()]
vl=len(value1)
if(length1==vl):
    print(*sorted(value1))
