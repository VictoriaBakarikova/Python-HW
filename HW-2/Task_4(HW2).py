user_input_1 = input("Input fist list of numbers: ")
user_input_2 = input("Input second list of numbers: ")
set_1 = set(map(int, user_input_1.split()))
set_2 = set(map(int, user_input_2.split()))
set_3 = set_1 | set_2
lst = []

diff = set_1.symmetric_difference_update(set_2)
difference_of_numbers_1 = set_1.difference(set_2)
difference_of_numbers_2 = set_2.difference(set_1)

intersection_numbers = set_1.intersection(set_2)

for number in set_3:
    if number not in intersection_numbers:
        lst.append(number)


print("Difference of numbers_1: ", difference_of_numbers_1)
print("Difference of numbers_2: ", difference_of_numbers_2)
print(diff)
print("Intersection of numbers: ", intersection_numbers)
print("list without difference: ", lst)
