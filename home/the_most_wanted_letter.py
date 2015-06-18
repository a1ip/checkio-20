def checkio(text):
    text = text.lower()
    total = 0
    letter = ''
    for i in text:
        if i.isalpha():
            if text.count(i) > total:
                letter = i
                total = text.count(i)
            elif text.count(i) == total:
                if i < letter:
                    letter = i
                    total = text.count(i)
    return letter
​
​
if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
