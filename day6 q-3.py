num=int(input("Enter a number:"))
count=0
while num:
    count+=num & 1
    num>>=1
    print("number of set bits=",count)
