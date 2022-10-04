def flatten(x):
    flat_list = []
    for sublist in x:
        for item in sublist:
            flat_list.append(item)
    return flat_list

print(flatten([[1,2],[3,4]]))

# SOLUTION_2:

def flatten(outer_list):
    result = []
    for inner_list in outer_list:
        for item in inner_list:
            result.append(item)
    return result

print(flatten([[1,2],[3,4]]))

def flatten(outter_list):
    return [
        item for inner_list in outter_list for item in inner_list
    ]