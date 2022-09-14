#Take the numberic portion of the given string and print it as an interger

str = "X-DSPAM-Confidence:0.9546"

col_index = str.find(":")
num = float(str[col_index+1:])
print(num)
print(str[:col_index])
