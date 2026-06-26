n=int(input("Enter number of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter element:")))
    print("Duplicate elements are:")
for i in range(n):
    for j in range(i+1,n):
     if arr[i]==arr[j]:
      print(arr[i])
      break