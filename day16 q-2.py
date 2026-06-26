n=int(input("Enter number of element:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter element:")))
    max_freq=0
    max_element=arr[0]
    for i in range(n):
        count=0
        for j in range(n):
            if arr[i]==arr [j] :
                count+=1
                if count>max_freq:
                    max_freq=count
                    max_element=arr[i]
                    print("Maximum frequency element=",max_element)
                    print("Frequency=",max_freq)



