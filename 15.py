'''
15.Write a program to print factorial number using function
'''

def factorial(num):
    num=int(input("Enter Number:"))
    fact=1  

    for i in range(1,num+1):
        fact=fact*i
        print(fact)  
    
factorial(12)
