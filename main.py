from stats import get_num_words, numbers_of_letters, build_sorted_letters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text():
    with open (book_path, "r") as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text()
    num_words = get_num_words(text)
    char_dict = numbers_of_letters(text)
    sorted_letters = build_sorted_letters(char_dict)
    print(f"Found {num_words} total words")
    for entry in sorted_letters:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    

main()