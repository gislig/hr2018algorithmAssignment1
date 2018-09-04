n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_num = 1
second_num = 2
third_num = 3

next_num = 0

# 1 + 2 + 3 = 6
# 2 + 3 + 6 = 11
# 3 + 6 + 11 = 20
# 6 + 11 + 20 = 37

# This is the formula
if n >= 1:
    print(first_num)

if n >= 2:
    print(second_num)

if n >= 3:
    print(third_num)

if n > 3:
    for seq in range(n-3):

        next_num = first_num + second_num + third_num
        first_num = second_num
        second_num = third_num
        third_num = next_num

        print(next_num)