aa=int(input())
cc=aa%60
dd=aa/60
ee=str(dd)
f=ee[:ee.index('.')]
f=int(f)
if(f<1):
    h=0 
    print(h,cc)
else:
    print(f,cc)
