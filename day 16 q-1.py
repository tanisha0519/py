n=int(input("Enter the number of elements:")) 
arr=[]
print("Enter n-1 elemnts")
for i in range(n-1):
    arr.append(int(input("Enter element:")))
    total=n*(n-1)//2
    arr_sum=sum(arr)
    missing=total-arr_sum
    print("Missing number=",missing)
    
