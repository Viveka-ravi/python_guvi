num = int(input())
st1 = []
for i in range(0,num):
    st = input()
    st1.append(st)

i = 0
c = 0
flag = True
for i in range(0,len(st1[0])):
    if(flag==False):
        break
    j=1
    while(j<num and st1[0][i]==st1[j][i]):
        j+=1
    if(j==num):
        c+=1
    else:
        flag = False
        break
    
for i in range(0,c):
    print(st1[0][i],end="")
