length=int(input())
value=[int(x) for x in input().split()]
vl=len(value)
if(length==vl):
    print(*sorted(value))
