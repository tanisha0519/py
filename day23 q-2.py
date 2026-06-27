str1=input("Enter string:")
for ch in str1:
    count=0
    for c in str1:
        if ch==c:
            count+=1
            if count > 1:
                print("First non repeating character:",ch)
                break
            else:
                print(" No non repeating character found")
