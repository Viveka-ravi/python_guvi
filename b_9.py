n, p = map(int,input().split())
s = list(input().split())
s = [int(x) for x in s]
sum = 0
for i in range(0,p):
   sum = sum + s[i]
print(sum)
