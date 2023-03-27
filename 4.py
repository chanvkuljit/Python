'''
4.Write a program to input Principal Amount, Rate and Year and 
display Compound Interest 
'''

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: " ))


Amount = principal * (pow((1 + rate / 100), time))
CI = Amount - principal
print("Compound interest is", CI)



