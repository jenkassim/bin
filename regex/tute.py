import scrabble
import re

def first_func()

    pattern = re.compile("uu")
    for word in scrabble.wordlist:
        if "uu" in word:
            print word

def second_func()

    pattern = re.compile("^[qwertasdfgzxcvb]*$")
    longest = ""

    for word in scrabble.wordist:
        if pattern.search(word) and len(word) > len(longest):
            longest = word

    print longest

