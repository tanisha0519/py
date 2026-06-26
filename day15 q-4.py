n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter element:")))
    count=0
    for i in range(n):
        if arr[i] !=0:
            arr[count]=arr[i]
            count += 1
            while count<n:
                arr[count]=0
                count +=1
                print("Array after moving zeroes to the end:")
                for i in arr:
                    print(i,end="")
                    


