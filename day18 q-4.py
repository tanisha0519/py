n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter element:")))
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]<arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                print("Array in descending order:")
                print(i,end="")
                