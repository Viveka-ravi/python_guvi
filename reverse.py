str = input()
str = list(str)
str_1 = ""
length = len(str)
leng = length-1
if(length%2 == 0):
  length = len(str)//2
else:
  length = len(str)//2+1
for i in range(0,length):
  temp = str[i]
  str[i] = str[leng-i]
  str[leng-i] = temp
str_1 = str_1.join(str)
print(str)
