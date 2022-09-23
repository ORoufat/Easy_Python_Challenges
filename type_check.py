# SOLUTION_1

def only_ints(a, b):
    return type(a) == int and type(b) == int


only_ints(1, 5) or only_ints(1, "b")


# SOLUTION_2

def only_ints(x, y):
    return type(x) == int and type(y) == int


print(only_ints(1, 1))
