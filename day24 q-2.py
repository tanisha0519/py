str1=input("Enter a string:")
resuly=""
count=1
for i in range(len(str1)):
    if i< len(str1)-1 and str1[i]==stri[i+1]:
        count+=1
    else:
        result+=str1[i]+str(count)
        count=1
        print("Compressed string:",result)
        