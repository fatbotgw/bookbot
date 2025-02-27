def word_count(book_text):
    count = 0
    word_list = book_text.split()

    for word in word_list:
        count += 1

    return count