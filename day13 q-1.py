n=int(input("Enter number of elements :"))
arr=[]
for i in range(n):
    element=int(input("Enter element:"))
    arr.append(element)
print("Array elements are:")
for i in arr:
    print(i,end=" ")
