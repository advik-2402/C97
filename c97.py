introstring= input("introduce yourself: ")
charactercount=0
wordcount=1
for i in introstring:
    charactercount += 1
    print(charactercount)
    if (i == " "):
        wordcount += 1
print("number of words in the string")
print(wordcount)
print("number of characters in the string")
print(charactercount)