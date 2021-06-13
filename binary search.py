print("MOHAMED AJAF's Binary Search ")
def binary_search(lst,k):
    l=0
    h=len(lst)-1
    m=0
    while l<=h:
        m=(l+h)//2
        if lst[m]<k:
            l=m+1
        elif lst[m]>k:
            h=m-1
        else:
            return m
    return -1
a=[5,9,12,14,23,31]
print(a)
k=int(input("Enter the Value to be Found:"))
result=binary_search(a,k)
if result!=-1:
    print('The element is found in',result+1,'position')
else:
    print("Element Not Found")
