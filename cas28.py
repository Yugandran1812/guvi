length=int(input())
str1 = [int(x) for x in input().split()]
if(length==len(str1)):
    for index, value in enumerate(str1):
        print(value, index)
