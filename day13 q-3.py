n=int(input("Enter number of element:"))
arr=[]
for i in range (n):
  element=int(input("Enter a element:"))
  arr.append(element)
  smallest=min(arr)
  largest=max(arr)
  print("Array elements",arr )
  print("Smallest element:",smallest) 
  print("Largest element:",largest)

