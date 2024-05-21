def main():
    path_to_book = "books/frankenstein.txt"  
    book = open_book(path_to_book)
    print(count_words(book))
       

def open_book(path_to_book):
    book = ""
    with open(path_to_book) as f: 
        book_contents = f.read()
        book = book_contents
    return book

def count_words(book):
    words = book.split()
    return len(words)
main()
