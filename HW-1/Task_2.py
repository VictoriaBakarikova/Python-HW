str_input=input("Введите слово: ")
wovels=['i', 'a', 'o', 'u', 'y', 'e']
result="".join(char for char in str_input if char not in wovels)
print(result)