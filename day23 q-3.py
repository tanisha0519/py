str1=input("Enter first string:")
str2=input("Enter second string:")
str1=str1.replace("","").lower()
str2=str2.replace("","").lower()
if len(str1)!=len(str2):
    print("Strings are not anagram")
    list1=list(str1)
    list2=list(str2)
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list2[i]>list2[j]:
                list2[i],list2[j],=list2[j],list[i]
                if list1==list2:
                    print("Strings are anagrams")
                else:
                    print("Strings are not anagram")
                    
