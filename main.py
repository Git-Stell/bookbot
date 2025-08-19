from stats import get_book_text, counting, characters_count, dictionary

def main():
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    num_words = counting(get_book_text("./books/frankenstein.txt"))
    print(f"Found {num_words} total words\n--------- Character Count -------")

    end = characters_count(get_book_text("./books/frankenstein.txt"))
    dictionary(end)



main()
