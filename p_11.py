num = int(input())
fact = 1
if(num%2 == 0):
    num_1 = num-1
    for i in range(1,num_1+1): 
        fact = fact * i 
    print (fact)
else:
    print(num)
        
