def isomo(st):
    result = ""
    i=0
    count=0
    while(i<len(st)):
        result = result + str(count)
        count = 0
        cha = st[i]
        while i<len(st) and st[i] == cha:
            count+=1
            i+=1
        count+=1
    return result

st = input()
st = st.split()
st1 = list(st[0])
st2=list(st[1])
num1=isomo(st1)
num2=isomo(st2)
if num1==num2:
    print("yes")
else:
    print("no")
