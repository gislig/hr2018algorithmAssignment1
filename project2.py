# 1. Checks if the first three numbers are entered
# 2. If the numbers are above 3 then start sequencing
# 3. Sums up the first, second and third number into a variable next_num 
# 4. Each step sets the last number to the next bellow
# 5. Finally it prints out the next_num

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

# Checks if the n is more or less than one
if n >= 1:
    print(first_num)

# Checks if the n is more or less than two
if n >= 2:
    print(second_num)

# Checks if the n is more or less than three
if n >= 3:
    print(third_num)

# If n is more than three then enter the if loop
if n > 3:
    # Sequence the numbers but remove the first three numbers because we have already gone through it
    for seq in range(n-3):

        # Sums up the first, second and third number into next number
        next_num = first_num + second_num + third_num
        first_num = second_num
        second_num = third_num
        third_num = next_num

        print(next_num)