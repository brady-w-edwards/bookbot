def main():
    bookPath = "books/frankenstein.txt"
    text = getBookText(bookPath)
    wordCount = countWords(text)
    print(f"The Frankenstein book contains {wordCount} words!")

def getBookText(path):
    with open(path) as f:
        return f.read()
        
def countWords(text):
    wordsArray = text.split()
    return len(wordsArray)

main()