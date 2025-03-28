str_input=input("Введите слово: ")
if str_input==str_input[::-1]:
    print("Palindrome")
else:
    print("ordinary word")