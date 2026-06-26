n=int(input("Enter the number of element:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter element:")))
    target=int(input("Enter the required sum:"))
    found=False
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                print("pair found:",arr[i],arr[j])
                found=True
                if not found:
                    print("No pair found")
                    