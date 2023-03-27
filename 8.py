'''
8.Write a Python Program to input marks of 4 subjects and 
display Total, Percentage, Result and Grade. If student is fail 
(<40) in any subject then Result should be displayed as “FAIL” 
and Grade should be displayed as “With Held**” 

'''

mark1=float(input("Enter Your Maths Mark:"))
mark2=float(input("Enter Your English Mark:"))
mark3=float(input("Enter Your Science Mark:"))
mark4=float(input("Enter Your Social Science Mark:"))

total=mark1+mark2+mark3+mark4
percentage=(total/400)*100

if((mark1<40) and (mark2<40) and (mark3<40) and (mark4<40)):
    print("Student is Fail.")
    
elif((mark1<=40 and mark1>=60) and (mark2<=40 and mark2>=60) and (mark3<=40 and mark3>=60) and (mark4<=40 and mark4>=60)):
    print("Student is Pass")
    print("Student Get C")
elif((mark1<=40 and mark1>=80) and (mark2<=40 and mark2>=80) and (mark3<=40 and mark3>=80) and (mark4<=40 and mark4>=80)):
    print("Student is pass")
    print("Student Get B")
    
elif((mark1<=40 and mark1>=100) and (mark2<=40 and mark2>=100) and (mark3<=40 and mark3>=100) and (mark4<=40 and mark4>=100)):
    print("Student is pass")
    print("Student Get A")
    
else:
    print("invalid Marks")
