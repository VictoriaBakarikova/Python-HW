cash=int(input("Введите сумму наличных купюр: "))
banknotes=[100, 50, 10, 5, 1]
for banknote in banknotes:
    count=cash//banknote
    cash%=banknote
    print(f"Вашу купюру можно разменять так: {banknote} рублей:{count}")