'''
9.Write a program to input a number and display Table of that 
number.
'''

num=int(input("Enter Number:"))

for i in range(1,11):
    print("{}x{} =".format(num,i),+(num*i))
