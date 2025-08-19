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

def sort_on(items):
    return items["num"]

result = []

def dictionary(sum_char):
    for i in sum_char:
        temp = {"char": i, "num": sum_char[i]}
        result.append(temp)
    result.sort(reverse=True, key=sort_on)
    for i in result:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


