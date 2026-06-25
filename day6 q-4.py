x=int(input("Enter base number(x):"))
n=int(input("Enter power number(n):"))
result=1
for i in range (n):
    result*=x
    print("result=",result)
