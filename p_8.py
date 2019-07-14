import math
x,y=map(int,input().split())
s=[]
r=list(map(int,input().split()))
for i in range(0,y):
    u_1,v_1=map(int,input().split())
    s.append([u_1,v_1])
for i in s:
    m=i[0]-1
    n=i[1]-1
    print(math.gcd(r[m],r[n]))
