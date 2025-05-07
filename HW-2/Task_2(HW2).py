user_input = input("Введите число: ")
numbers = user_input.split()

uniq_numbers = set(numbers)

repeated_numbers = set(
    [number for number in numbers if numbers.count(number) > 1]
)

even_numbers = []
odd_numbers = []
for number in numbers:
    try:
        if float(number).is_integer():
            number = int(float(number))
            if int(number) % 2 == 0:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)
    except ValueError:
        print("Skip float number")

negative_numbers = set([number for number in numbers if float(number) < 0])

float_numbers = set(
    [
        float(number)
        for number in numbers
        if float(number) != int(float(number))
    ]
)

sum_of_aliquot_numbers = sum(
    int(float(number))
    for number in numbers
    if float(number).is_integer() and int(float(number)) % 5 == 0
)

max_number = max([float(number) for number in numbers])
min_number = min([float(number) for number in numbers])

print("Uniq numbers: ", list(uniq_numbers))
print("Repeated numbers: ", list(repeated_numbers))
print("Even numbers: ", even_numbers)
print("Odd numbers: ", odd_numbers)
print("Negative number: ", negative_numbers)
print("Float_numbers: ", float_numbers)
print("Sum of multiples of 5 = ", sum_of_aliquot_numbers)
print("Max number = ", max_number)
print("Min number = ", min_number)
