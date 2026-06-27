str1=input("Enter a string:")
vowels=0
consonants=0
for ch in str1:
    if ch.isalpha():
        vowels += 1
    else:
        consonants+=1
        print("Number od vowels:",vowels)
        print("Number of consonants:",consonants)
