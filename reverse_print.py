# Write a code that prints the elements reverse. Example: apple ==> elppa

fruits = ["apple", "peach", "pear"]
new_list = []

for i in fruits:
    for j in i:
        j = i[::-1]
    new_list = j
    print(new_list)
