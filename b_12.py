n = input()
res = [str(x) for x in n]
res.reverse()
#for x in res:
pal = ("".join(res)) 
if(pal == n):
    print('yes')
else:
    print("no")
