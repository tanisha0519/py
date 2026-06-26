n=int(input("Enter the number of element:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element:")))
    unique=[]
    for i in arr:
        if i not in unique:
            unique.append(i)
            print("Array after removing duplicate:")
            for i in unique:
                print(i,end="")
                