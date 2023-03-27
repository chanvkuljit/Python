'''
3.Write a program to input Principal Amount, Rate and Year and 
display Simple Interest. 
'''
Principal=float(input("Enter Principal Amount:"))
Rate=float(input("Enter Rate Of Interest:"))
Year=float(input("Enter Number Of Year:"))

SI=(Principal*Rate*Year)/100

print("{} Is A Simple Interest Of Given Data.".format(SI))
