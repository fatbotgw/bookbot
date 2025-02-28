def word_count(book_text):
    count = 0
    word_list = book_text.split()

    for word in word_list:
        count += 1

    return count


def character_count(text_string):
    counts = {}

    for letter in text_string:
        if letter.lower() in counts:
            counts[letter.lower()] += 1
        else:
            counts[letter.lower()] = 1

    return counts


def sort_on(dict_item):
    # Get the first (and only) key in the dictionary
    key = list(dict_item.keys())[0]
    # Return the value associated with that key
    return dict_item[key]


def dict_sort(dictionary):
    sorted_list = []  # this is a list of dictionaries

    # This works, but isn't very Python-like
    # for entry in dictionary:
    #     if entry.isalpha() is True:
    #         sorted_list.append({entry:dictionary[entry]})

    # This way of iterating through key-value pairs is the more Python way
    for key, value in dictionary.items():
        if key.isalpha() is True:
            sorted_list.append({key: value})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
