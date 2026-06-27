sentence=input("Enter a sentence:")
word=sentence.split()
longest=word[0]
for word in word:
    if len(word)>len(longest):
        longest= word
        print("Longest word:",longest)
        print("Length:",len(longest))