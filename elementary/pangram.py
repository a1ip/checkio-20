from string import ascii_lowercase
​
def check_pangram(text):
    ln = 0
    for i in ascii_lowercase:
        if i in text.lower():
            ln += 1
    return ln == 26

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"

​"""
def check_pangram(text):
    return set(ascii_lowercase).issubset(set(text.lower()))
​"""
