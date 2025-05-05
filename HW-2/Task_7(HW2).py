user_input = input("Input the string: ")
letters = list(user_input)

letter_count = 1
new_list = []

for i in range(1, len(user_input)):
    if user_input[i] == user_input[i - 1]:
        letter_count += 1
    else:
        new_list.append(user_input[i - 1] + str(letter_count))
        letter_count = 1
new_list.append(user_input[-1] + str(letter_count))


print("".join(new_list))
