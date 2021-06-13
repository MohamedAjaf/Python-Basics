n1=int(input("Enter limit: "))
print("Prime numbers: ",end=' ')
for n in range(1,n1):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n,end=' ')
