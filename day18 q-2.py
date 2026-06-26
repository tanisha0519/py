n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter element:")))
    for i in range(n):
        mis_index=i
        for j in range(i+1,n):
          if arr[j]<arr[min_index]:
            min_index=j
            temp=arr[i]
            arr[i]=arr[min_index]
            arr[min_index]=temp
    print("Sorted array:")
    for i in arr:
        print(i,end="")


