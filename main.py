# book bot

def countChars(text):
    lowtext = text.lower()
    alphabet = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0, }
    # ok i found a list comprehesion via search engine. i can't claim that i'am happy with it because really feel safe with list comprehesions.
    # but a oneliner rather than a stupid repeat of if elif statements. it was worth it.
    # here's the line i used from https://pythonguides.com/python-dictionary-increment-value/
    # ticket_prices = {city: price + 20 if city == increase_city else price for city, price in ticket_prices.items()}
    for i in lowtext:
        alphabet = {char: count + 1 if char == i else count for char, count in alphabet.items()}
    return alphabet
    
def count_words(text):
    words = text.split()
    count = len(words)
    return count

def openBook(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def printBook(text):
    print(text)

def sort_dict(dict):
    sorted_dict = {key: value for key, value in sorted(dict.items(), key=lambda item: item[1])}
    return sorted_dict

def rev_sort_dict(dict):
    sorted_dict = {key: value for key, value in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
    return sorted_dict

def report(book):
    text = openBook(book)
    charList = countChars(text)
    sorted = rev_sort_dict(charList)
    words = count_words(text)
    print(f"--- Begin Report of {book} ---")
    print(f"{words} found in the document\n")
    for k, v in sorted.items():
        print(f"The '{k}' character was found {v} times")


def main():
    # using a constant value for now
    book = "books/frankenstein.txt"
    report(book)

if __name__ == "__main__":
    main()
