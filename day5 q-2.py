num=int(input("Enter a number:"))
original=num
sum_factors=0
while num>0:
    digit=num%10
    factor=1
    for i in range(1,digit+1):
        factor*=i
    sum_factors+=factor
    num//=10
if sum_factors==original:
    print("It is a strong number.")
else:
    print("It is not a strong number.")