# SOLUTION_1

def add_dots(string):
    new_string = ".", join(string)
    return new_string


print(add_dots("test"))


def remove_dots(string):
    new_string = string
    result = new_string.replace(".", "")
    return result


print(remove_dots("t.e.s.t"))
print(remove_dots(add_dots("tito")))


# SOLUTION_2


def add_dots(s):
    return ".".join(s)


def remove_dots(s):
    return s.replace(".", "")
