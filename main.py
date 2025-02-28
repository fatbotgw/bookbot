from stats import word_count
from stats import character_count

def get_book_test(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    book_location = "books/frankenstein.txt"
    book = get_book_test(book_location)
    words = word_count(book)

    print(f"{words} words found in the document")
    print(character_count(book))

main()
