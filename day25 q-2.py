str1=input("enter first string:")
str2=input("Enter second string:")
common=""
for ch in str1:
    if ch in str2 and ch not in common:
        common+=ch
        if common:
            print("common characters=",common)
        else:
            print("no common character found")