from itertools import combinations
x,y=map(int,input().split())
m=len(str(x))
str_1 = list(combinations(str(x),m-y))
str_1 = sorted(str_1)
print(*str_1[0],sep='')
