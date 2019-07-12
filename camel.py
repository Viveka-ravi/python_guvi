st = input()
st = list(str(st))
for i in range(0,len(st),2):
    st[i] = st[i].capitalize()

print("".join(map(str, st)))
