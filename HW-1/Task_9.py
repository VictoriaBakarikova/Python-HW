float_number_1=float(input("Введите дробное число 1: "))
float_number_2=float(input("Введите дробное число 2: "))
difference=abs(float_number_1-float_number_2)
if difference < 0.001:
    print("True")
else:
    print("False")