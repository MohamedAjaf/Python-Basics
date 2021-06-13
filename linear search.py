print("MOHAMED AJAF's Linear Search ")
def linear_search(lst,key,n):
    for i in range(n):
        if lst[i]==key:
            return i
    else:
        return -1
a=[1,3,5,4,7,9]
print(a)
k=int(input("Enter the Value to be Found:"))
n=len(a)
result=linear_search(a,k,n)
if result==-1:
    print("Element Not Found")
else:
    print('The element is found in',result+1,'position')





