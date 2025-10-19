import sys
from stats import get_num_words
from stats import count_chars
from stats import print_counts

def get_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    text = get_book(path)
    get_num_words(text)
    counts = count_chars(text)
    print_counts(counts)
main()
