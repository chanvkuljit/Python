'''
10.Write a program to print all numbers which are divisible by 7 
between 1 to 200
'''
num=[]

for i in range(1,200):
    if(i%7==0):
        num.append(str(i))
        print (','.join(num))
    
