user_input = input("Input numbers: ")
numbers = user_input.split()

new_list = []

for number in numbers:
    if number not in new_list:
        new_list.append(number)

print("New list withot repeats: ", new_list)
