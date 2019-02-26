length=int(input())
value=[int(x) for x in input().split()]
vl=len(value)
if(length==vl):
    a=sorted(value)
    b=round((vl-1)/2)
    c=a[b]
    print(c)
