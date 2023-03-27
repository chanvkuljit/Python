'''
12.Write a program to input a number and display whether number is prime or not.
'''

num=int(input("Enter Number:"))
ch=-0

if(num>1):
    for i in range(2,num):
        if(num%i==0):
            ch=1
        break

if(ch==1):
    print("Number is Not Prime",+num)
else:
    print("Number is Prime",+num)
