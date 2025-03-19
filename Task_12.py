decimla_number=int(input("Введите число: "))
binary_number=""
while decimla_number>0:
    binary_number=str(decimla_number % 2) + binary_number
    decimla_number=decimla_number//2
print(f"Число в бинарной системе: {binary_number}")
new_decimal_number=0
power=0
for i in reversed(binary_number):
    new_decimal_number += int(i)*(2**power)
    power+=1
print(f"Число в десятичной системе: {new_decimal_number}")

