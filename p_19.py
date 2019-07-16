n = int(input())
s1 = []
for i in range(0,n):
    s = list(input().split())
    s1 = s + s1        


s1.sort()
res = (' '.join(s1))
print(res,end=" ")
