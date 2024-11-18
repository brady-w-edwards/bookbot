def main() :
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        def countWords() :
            wordsArray = file_contents.split()
            words = wordsArray.__len__()
            print("The Frankenstein book contains " + str(words) + " words!")
        
        countWords()

main()