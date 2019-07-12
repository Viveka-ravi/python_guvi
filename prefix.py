num = int(input())
string = []
for i in range(0,num):
    st = input()
    string.append(st)

i = 0
c = 0
flag = True
for i in range(0,len(string[0])):
    if(flag == False):
        break
    k = 1
    while(k < n and string[0][i] == string[k][i]):
        k+=1
    if(k == n):
        c+=1
    else:
        flag = False
        break
    
for i in range(0,c):
    print(string[0][i],end="")
