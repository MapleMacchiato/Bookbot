def main():
    path_to_book = "books/frankenstein.txt"  
    book = open_book(path_to_book)
    word_count = count_words(book)
    letter_count = count_letters(book)
    print_report(letter_count, path_to_book, word_count)


def open_book(path_to_book):
    book = ""
    with open(path_to_book) as f: 
        book_contents = f.read()
        book = book_contents
    return book

def count_words(book):
    words = book.split()
    return len(words)

def count_letters(book):
    char_count = {}
    for c in book:
        lc = c.lower()
        if lc in char_count:
            char_count[lc] += 1 
        else:
            char_count[lc] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def print_report(char_count, path_to_book, word_count):
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{word_count} words found in the document")
    chars_list = []
    print(type(chars_list))
    for c in char_count:
        if c.isalpha():
            chars_list.append({"char": c, "num": char_count[c]})
    chars_list.sort(reverse=True, key=sort_on)
    for i in range(len(chars_list)):
        c = chars_list[i]["char"]
        n = chars_list[i]["num"]
        print(f"The '{c}' character was found {n} times")
    print("--- End of Report ---")
main()
