n1=int(input("Enter the number of element:"))
arr1=[]
for i in range(n1):
    arr1.append(int(input("enter the element:")))
n2 =int(input("Enter the number of element:"))
arr2=[]
for i in range(n2):
        arr2.append(int(input("Enter the element:")))
        arr3=arr2+arr1
        print("Merged array:")
        for i in arr3:
              print(i,end="")

