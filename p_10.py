num = int(input())
list_1 = list(map(int,input().split()))
c = 0
for i in range(0,num):
    for j in range(0,i):
        if list_1[j] < list_1[i]:
            c = c+list_1[j]
print(c)
