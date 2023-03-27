"""Write a Python Program accept comma separated string and
 display tokens using split(), rsplit() and splitlines()"""

string1=("hola, ich bin kuldeep\n arigato")

output=string1.split(",")
print(output)

output1=string1.rsplit()
print(output1)

output2=string1.splitlines()
print(output2)