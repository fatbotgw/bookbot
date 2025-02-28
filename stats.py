def word_count(book_text):
    count = 0
    word_list = book_text.split()

    for word in word_list:
        count += 1

    return count


def character_count(text_string):
    pass
    counts = {}

    for letter in text_string:
        if letter.lower() in counts:
            counts[letter.lower()] += 1
        else:
            counts[letter.lower()] = 1

    return counts
