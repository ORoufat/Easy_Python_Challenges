# SOLUTION_1
def double_letters(string):
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i + 1]
        if letter1 == letter2:
            return True
    return False


print(double_letters("HELLO"))


# SOLUTION_2
def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])


print(double_letters("HELLO"))
