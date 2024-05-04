def main():
    book_path = "/home/user/workspace/github.com/trevmcar/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = char_counter(text)
    letter_count.sort(reverse=True, key=sort_char_count)
    print(f"--- Begin report of {book_path}")
    print(f"Your document has {word_count} words!\n")
    for letters in letter_count:
        letter = letters["letter"]
        num = letters["num"]
        print(f"The '{letter}' character was found {num} times!")
    print("\n--- End Report ---")
   

def get_word_count(text):
    words = text.split()
    return len(words)


def char_counter(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    letter_count = []
    for key, value in char_count.items():
        letter_value = {"letter": key,
                        "num": value}
        letter_count.append(letter_value)
    return letter_count


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def sort_char_count(char_count):
    return char_count["num"]

main()
