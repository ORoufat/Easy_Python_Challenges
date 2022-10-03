""" 
Two strings are anagrams if you can mae one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. Your function should return True
if the strings are anagrams and False otherwise.

For Example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", 
"Bob") should return False. 

"""


# SOLUTION_1
def isAnagram(text1, text2):
    str1_list = list(text1)
    str1_list.sort()
    str2_list = list(text2)
    str2_list.sort()

    return str1_list == str2_list


print(isAnagram('pythoon', 'opython'))


# SOLUTION_2:

def is_anagram(text1, text2):
    return sorted(text1) == sorted(text2)


print(is_anagram('pythoon', 'opython'))


# SOLUTION_3:


def count_letters(string):
    return {l: string.count(l) for l in string}


def is_anagram(string1, string2):
    return count_letters(string1) == count_letters(string2)


print(is_anagram('pythoon', 'opython'))
