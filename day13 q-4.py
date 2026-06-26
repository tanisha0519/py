n=int(input("Enter number of element:"))
arr=[]
for i in range(n):
    element=int(input("Enter a element:"))
    arr.append(element)
    even=0
    odd=0
    for i in arr:
        if i%2==0:
            even+=1
        else:
            odd+=1
print("Array elements:",arr)
print("even element:",even)
print("Odd elements:",odd)
