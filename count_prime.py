def prime(num):
    i = 2
    while(i < num):
        if num%i == 0:
            return False
        i+=1
    return(True)

num = input()
num = num.split()
num1 = int(num[0])
num2 = int(num[1])
count = 0
while(num1<=num2):
    if(prime(num1)):
        count+=1
    num1+=1
print(count)
