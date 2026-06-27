str1=input("Enter a string:")
for ch in str1:
    count=0
    for c in str1:
        if ch==c:
            count+=1
            print(ch,"=",count)