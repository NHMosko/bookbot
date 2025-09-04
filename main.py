from stats import count_words, count_characters, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_num = count_words(book_text)
    char_dict = count_characters(book_text)
    sorted_chars = sort_dict(char_dict)

    print("============ BOOKBOT ============\n" 
          f"Analyzing book found at {filepath}...\n"
          "----------- Word Count ----------\n"
          f"Found {word_num} total words\n"
          "--------- Character Count -------\n")
    for i in sorted_chars:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()
