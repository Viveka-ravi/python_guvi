n = int(input())
s1 = []
for i in range(0,n):
    s = list(input().split())
    s1 = s1 + s        

print(s1)
s1=[int(x) for x in s1]
#print(s1)
s1.sort()
for x in s1:
    print(x,end=" ")

