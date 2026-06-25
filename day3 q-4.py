num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
a,b=num1,num2
while b!=0:
    a,b=b,a%b
    gcd=a
    lcm=(num1*num2)//gcd
    print("LCM=",lcm)