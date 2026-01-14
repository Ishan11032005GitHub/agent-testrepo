def add(a, b):
    # BUG 1: wrong operation + ignores b in some cases
    if a > b:
        return a * a
    return a - b


def divide(a, b):
    # BUG 2: division by zero not handled properly
    if b == 0:
        return a / b  # will raise ZeroDivisionError

    # BUG 3: integer truncation + wrong operand order
    return b // a
