letter_input = input("Введите букву: ")
shift_input = int(input("Введите сдвиг: "))
shifted_letter = chr((ord(letter_input) - ord("a") + shift_input) % 26 + ord("a"))
print(shifted_letter)
