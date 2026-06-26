n=int(input("Enter number of elements:"))
arr=[]
for i in range(n):
    element=int(input("Enter element:"))
    arr.append(element)
    total=sum(arr)
    print("Array elements",arr)
    print("sum of arrayelements=",total)