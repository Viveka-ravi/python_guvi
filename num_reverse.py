str_1 = int(input())
str_1 = list(str(str_1))
str_2 = ""
length = len(str_1)
leng = length-1
if (length%2 == 0):
  length = len(str_1)//2
else:
  length = len(str_1)//2+1
for i in range(0,length):
  temp = str_1[i]
  str_1[i] = str_1[leng - i]
  str_1[leng - i] = temp
str_2 = str_2.join(str_)
print(int(str_2))
