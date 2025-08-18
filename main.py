from stats import get_book_text, counting, characters_count

def main():
    num_words = counting(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    end = characters_count(get_book_text("./books/frankenstein.txt"))
    print(f"{end}")
main()
