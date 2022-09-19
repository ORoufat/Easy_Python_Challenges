"""CAPITAL INDEXES

WRITE A FUNCTION NAMED CAPITAL_INDEXES. tHE FUNCTION TAKES A SINGLE PARAMETER WHICH IS A STRING.
YOUR FUNCTION SHOULD RETURN A LIST OF ALL THE INDEXES IN THE STRING THAT HAVE CAPITAL LETTERS.
FOR EXAMPLE:: CAPITAL_INDEXES("HeLlO") SHOULD RETURN THE LIST [0,2,4]
"""
# SOLUTION:

test = 'TEsT'

res = [i for i in range(len(test)) if test[i].isupper()]
print(res)


# SOLUTION_2:
def capital_indexes(test):
    res = [i for i in range(len(test)) if test[i].isupper()]
    return res


capital_indexes('HeLlO')
