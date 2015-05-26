def checkio(n, m):
    # ^ Binary XOR - It copies the bit if it is set in one operand but not both.
    return bin(n ^ m).count('1')
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"

