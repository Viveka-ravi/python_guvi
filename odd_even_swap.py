st = input()
st = list(st)
result = ""
for i in range(0,len(st)-1,2):
    temp=st[i+1]
    st[i+1]=st[i]
    st[i]=temp
print(result.join(st))
