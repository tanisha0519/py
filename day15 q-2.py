n=int(input("Enter number of elemnts:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter element:")))
    first=arr[0]
    for i in range (n-1):
        arr[i]=arr[i+1]
    arr [n-1] = first
print("Array after left rotation:")
for i in arr:
    print(i,end="")
