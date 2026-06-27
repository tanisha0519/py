sentence=input("Enter a sentence:")
words=sentence.split()
n=len(words)
for i in range(n-1):
    for j in range(n-1-i):
        if len(words[j])>len(words[j+1]):
            temp=words[j]
            words[j]=words[j+1]
            words[j+1]=temp
            print("Words sorted by length:")
            for words in words:
                print(words)



