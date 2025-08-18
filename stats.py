def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def counting(book):
    words = book.split()
    num = len(words)
    return num

sum_char = {}

def characters_count(file_contents):
    lower_char = file_contents.lower()
    for word in lower_char:
        if word in sum_char:
            sum_char[word] += 1
        else:
            sum_char[word] = 1
    return sum_char
