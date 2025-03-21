def int_to_roman(num):
    roman_numbers=[
    ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
    ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]
    result=""
    for roman, arabic in roman_numbers:
        while num>arabic:
            result+=roman
            num-=arabic
    return result
user_input=int(input("Введите число от 1 до 100: "))
if 0<user_input<=100:
    print(int_to_roman(user_input))
else:
    print("Неправильно введено число")
