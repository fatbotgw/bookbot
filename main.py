from stats import word_count
from stats import character_count
from stats import dict_sort
import sys


def get_book_test(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_location = sys.argv[1]
    book = get_book_test(book_location)
    words = word_count(book)

    word_list = dict_sort(character_count(book))
    # print(f"{words} words found in the document")
    # print(character_count(book))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for word in word_list:
        for key in word:
            print(f"{key}: {word[key]}")
    print("============= END ===============")


main()
