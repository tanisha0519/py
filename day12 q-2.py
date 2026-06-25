def armstrong(num):
    temp=num
    digits=len(str(num))
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**digits
        temp//=10
        if sum==num:
            print(num,"Is an armstrong number:")
        else:
            print(num,"Is not an armstrong number:")
n=int(input ("Entar a number:"))
armstrong (n)
