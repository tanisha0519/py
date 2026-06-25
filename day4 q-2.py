n=int(input("Enter a term number:"))
a,b=0,1
if n<=0:
    print("Invalid input")
elif n==1:
    print(" Nth Fibonacci term=",a)
elif n==2:
    print("Nth Fibonacci term=",b)
else:
    for i in range(3,n+1):
        a,b=b,a+b
    print("Nth Fibonacci term=",b)