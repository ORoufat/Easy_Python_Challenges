import random
num_list = []
for i in range(5):
    num_list.append(random.randrange(1, 9))
i = len(num_list) - 1

while i > 1:
    j = 0
    while j < i:
        print("\nIS {} > {}".format(num_list[j], num_list[j + 1]))
        print()
        if num_list[j] > num_list[j + 1]:
            print("SWITCH")
            temp = num_list[j]
            num_list[j] = num_list[j + 1]
            num_list[j + 1] = temp
        else:
            print("Dont Switch")
        j += 1
        for k in num_list:
            print(k, end="")
            print()
    print("end of round")
    i -= 1
    for k in num_list:
        print(k, end="")
    print()

