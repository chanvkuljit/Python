"""Write a program that accepts sequence of lines as input and prints the lines ,
after making all characters in the sentence capitalized. If you enter blank line,
shall be treated as exit of program. All the upper case converted lines shall be added 
to list one by one"""

lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)