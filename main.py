def main():
    bookPath = "books/frankenstein.txt"
    text = getBookText(bookPath)
    wordCount = countWords(text)
    letterCount = countCharacters(text)
    print(f"The Frankenstein book contains {wordCount} words!")
    print(letterCount)

def getBookText(path):
    with open(path) as f:
        return f.read()
        
def countWords(text):
    wordsArray = text.split()
    return len(wordsArray)

# def countCharacters(text):
#     characterList = text.strip()
#     lowercaseList = characterList.lower()
#     return len(lowercaseList)

def countCharacters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


main()