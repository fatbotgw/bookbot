from stats import word_count
from stats import character_count
from stats import dict_sort

def get_book_test(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    book_location = "books/frankenstein.txt"
    book = get_book_test(book_location)
    words = word_count(book)

    word_list = dict_sort(character_count(book))
    # print(f"{words} words found in the document")
    # print(character_count(book))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for word in word_list:
        for key in word:
            print(f"{key}: {word[key]}")
    print("============= END ===============")

main()
