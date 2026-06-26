n=int(input("Enter number of elements:"))
arr=[]
for i in range (n):
    element=int(input("Enter element:"))
    arr.append(element)
key=int(input("Enter element to find frequency:"))
count=0
for i in arr:
    if i == key: 
     count += 1
    print("Frequency of",key,"=",count)

