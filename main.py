# book bot

def countChars(book):
    text = openBook(book)
    lowtext = text.lower()
    alphabet = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0, }
    
    # ok i found a list comprehesion via search engine. i can't claim that i'am happy with it because really feel safe with list comprehesions.
    # but a oneliner rather than a stupid repeat of if elif statements. it was worth it. here's the line i used from https://pythonguides.com/python-dictionary-increment-value/
    # ticket_prices = {city: price + 20 if city == increase_city else price for city, price in ticket_prices.items()}
    for i in lowtext:
        alphabet = {char: count + 1 if char == i else count for char, count in alphabet.items()}
    return alphabet
    
def countWords(book):
    text = openBook(book)
    words = text.split()
    count = len(words)
    return count

def openBook(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def printBook(book):
    with open(book) as f:
        file_contents = f.read()
        print(file_contents)

def report(book):
    pass


def main():
    # using a constant value for now
    book = "books/frankenstein.txt"
    #printBook(book)
    #print(countWords(book))
    print(countChars(book))
    #countChars(book)

if __name__ == "__main__":
    main()
