from stats import get_book_text, counting, characters_count, dictionary
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    num_words = counting(get_book_text(f"./{sys.argv[1]}"))
    print(f"Found {num_words} total words\n--------- Character Count -------")

    end = characters_count(get_book_text(f"./{sys.argv[1]}"))
    dictionary(end)



main()
