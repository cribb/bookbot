import stats as mystats
import sys 

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def main(filepath):
    book = get_book_text(filepath)
    count = mystats.get_num_words(book)

    letter_dict = mystats.get_num_letters(book)
    # for letter in letter_dict:
    #     letter_count = letter_dict[letter]
    #     print(f"'{letter}': {letter_count}")

    sorted_list = mystats.sort_by_frequency(letter_dict)    

    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("---------- Word Count ----------")
    print(f"Found {count} total words")
    print("---------Character Count -------")
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")

    return letter_dict


argv = sys.argv

if len(argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(argv[1])





