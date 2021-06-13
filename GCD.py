a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
if(a>b):
    n=b
else:
    n=a
for i in range(1,n+1):
    if((a%i==0) and (b%i==0)):
        g=i
print("GCD of",a,"and",b,"is",g)
