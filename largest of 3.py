n1 = int(input())
n2 = int(input())
n3 = int(input())

if (n1>=n2) and (n1>=n3):
 largest = n1
elif (n2 >= n1) and (n2 >= n3):
 greatest = n2
else:
 greatest = n3

 
print("The greatest number is",greatest )
