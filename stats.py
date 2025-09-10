# stats.py

def get_num_words(book):
    words = book.split()
    num_words = len(words)

    return num_words

def get_num_letters(book):
    
    letter_counts = {}

    for letter in book:
        
        my_letter = letter.lower()

        if my_letter in letter_counts:
            letter_counts[my_letter] += 1
        else:
            letter_counts[my_letter] = 1

    return letter_counts

def sort_on(items):
    return items["num"]

def sort_by_frequency(letter_counts):
    
    letter_list = []

    for letter in letter_counts:
        letter_db = {}

        if letter.isalpha():
            letter_db["char"] = letter
            letter_db["num"] = letter_counts[letter]

            # print(f"Adding {letter} value of {letter_counts[letter]}")
            letter_list.append(letter_db)

    letter_list.sort(key=sort_on, reverse=True)

    return letter_list