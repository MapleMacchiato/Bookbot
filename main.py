def main():
    path_to_book = "books/frankenstein.txt"  
    book = open_book(path_to_book)
    print(count_words(book))
    print(count_letters(book))

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
main()
