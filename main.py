def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)

    character_count = char_dictionary(text)
    letter_count = get_letter_count(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} found in the document\n")
    
    for letter in letter_count:
        if letter.isalpha():
            number = letter_count[letter]
            print(f"The {letter} was found {number} times in the document")

def sort_on(d):
    return d["num"]

def get_letter_count(char_dict):
    new_char_dict = {}
    for ch in char_dict:
        new_char_dict.append(char_dict[ch])

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def count_words(text):
    words_array = text.split()
    return len(words_array)

# def countCharacters(text):
#     characterList = text.strip()
#     lowercaseList = characterList.lower()
#     return len(lowercaseList)

def char_dictionary(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


main()
