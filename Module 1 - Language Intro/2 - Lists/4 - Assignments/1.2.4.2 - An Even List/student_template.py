import random

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""

# randomly sample a distribution between 2 and 6
random_number = int(random.uniform(2, 6))

# any number times 2 is even
an_odd_number = 2 * random_number

# generate a random list of odd length containing values up to 100
even_list = random.sample(range(100), an_odd_number)

# print out the list contents
print("Your list is: ", even_list)

"""
YOUR CODE BEGINS BELOW HERE. FILL IN THE MISSING OPERATIONS / CODE
"""
even_length = len(even_list)

middle_index = int(even_length / 2)
middle_value = even_list[middle_index]
left_middle_value = even_list[middle_index - 1]

print(middle_value,left_middle_value)

# this is the final result. Modify this line, and the empty lines above, to solve the assignment
middle_average = (middle_value + left_middle_value) / 2

# the average of middle elements is
print("The average is: ", middle_average)
