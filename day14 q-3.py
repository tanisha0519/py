n=int(input("Enter number of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a elemnt::")))
    largest=arr[0]
    smallest=arr[0]
    for i in arr:
        if i>largest:
         largest = i
for i in arr:
    if i > second and i != largest:
        second=i
        print("Largest element:",largest)
        print("second largest element:",second)
