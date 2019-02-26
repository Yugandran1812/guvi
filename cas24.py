lfs=int(input())
value=[int(x)for x in input().split()]
if(lfs==len(value)):
    value=sorted(value)
    print(*value)
