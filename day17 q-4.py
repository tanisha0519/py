n1=int(input("Enter the number of element:"))
arr1=[]
for i in range(n1):
    arr1.append(int(input("enter the element:")))
n2 =int(input("Enter the number of element:"))
arr2=[]
for i in range(n2):
        arr2.append(int(input("Enter the element:")))
print("Common elements are:")
for i in arr1:
      if i in arr2:
            print(i,end="")
            