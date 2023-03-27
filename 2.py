'''
2.Write a program to input 2 number and an arithmetic operator. 
Display the result accordingly. 
'''

num1=int(input("1 Number:"))
num2=int(input("2 Number:"))

addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
division=num1/num2
modules=num1%num2
power=num1**num2

print("{} is  addition of two number".format(addition))
print("{} is subtraction of two number".format(subtraction))
print("{} is multiplication of two number".format(multiplication))
print("{} is division of two number".format(division))
print("{} is modules of two number".format(modules))
print("{} is power of two number".format(power))
