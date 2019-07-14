a = int(input())
b = []
c = 0
for i in range (0,a+1):
    c = abs((2**i)-a)
    b.append(c)
print(min(b))
