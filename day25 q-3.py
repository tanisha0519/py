n=int(input("enter number of names:"))
names=[]
for i in range(n):
    names.append(input("Enter a name:"))
    for i in range(n-1):
        for j in range(n-1-i):
            if names[j]>names[j+1]:
                temp=names[j]
                names[j]=names[j+1]
                names[j+1]=temp
                print("Names in alphabetical orde:")
                for name in names:
                    print(name)
