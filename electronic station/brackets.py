def checkio(expression):
    op = ['(', '[', '{']
    cl = [')', ']', '}']
    stack = []
    for e in expression:
        if e in op: stack.append(e)
        if e in cl:
            if len(stack) == 0: return False
            top = stack.pop()
            if op.index(top) != cl.index(e): return False
    if len(stack) != 0: return False
    return True

if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
