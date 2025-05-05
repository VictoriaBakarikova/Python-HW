number = input("Введите число: ")
sum_of_number = 0
for i in number:
    sum_of_number += int(i)
if sum_of_number % 7 == 0:
    print("Magic!")
else:
    print(sum_of_number)
