print("MOHAMED AJAF's PROGRAM")
n = int(input("enter the total number of elements to be stored in the list: "))
list=[]
print("enter the elemnet one by one:")
for i in range(0,n):
    list.append(int(input()))
print(list)
max = list[0]
min = list[0]
for i in list:
    if(max <= i):
        max = i
    if(min >= i):
        min = i
print("the maximum element in the list is {0}".format(max))
print("the minimum element in the list is {0}".format(min)) 
                

