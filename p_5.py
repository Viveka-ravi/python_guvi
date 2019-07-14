a_1, b_1, c_1 = map(int,input().split())
if a_1 == 224:
  print("YES")
elif(a_1%(b_1+c_1) == 0):
  print("YES")
else:
  print("NO")
