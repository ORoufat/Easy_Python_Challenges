# SOLUTION_1

def count(word):
    new_word = word
    count_syllables = new_word.split('-')
    return len(count_syllables)


print(count("ho-tel"))


# SOLUTION_2

def count(word):
    syllables = 1
    for letter in word:
        if letter == "-":
            syllables = syllables + 1
    return syllables


# SOLUTION_3

def count(word):
    return word.count("-") + 1


def count(word):
    return len(word.split("-"))
