num=int(input("Enter a number:"))
product=1
while num>0:
    product *= num%10
    num//=10
    print("product of digits=",product)
    