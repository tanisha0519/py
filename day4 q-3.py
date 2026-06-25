num=int(input("Enter a number:"))
original=num
n=len(str(num))
sum_digits=0
while num>0:
    digit=num%10
    sum_digits+=digit**n
    num//=10

if sum_digits==original:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
