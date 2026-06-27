str1=input("Enter string:")
max_count=0
max_char=""
for ch in str1:
    count=0
    for c in str1:
        if ch==c:
            count+=1
            if count>max_count:
                max_count=count
                max_char=ch
                print("Maximum occuring character:",max_char)
                print("frequency=",max_count)
