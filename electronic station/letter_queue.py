def letter_queue(commands):
    queue = []
    for elements in commands:
        command = elements.split()
        if command[0] == 'PUSH':
            queue.append(command[1])
        else:
            queue = queue[1:]
    return ''.join(queue)

if __name__ == '__main__':
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
