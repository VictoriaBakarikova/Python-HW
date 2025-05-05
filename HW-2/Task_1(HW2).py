import re

str_input = input("Введите строку: ")
words = re.split(r"[ ,.]+", str_input)
word_count = {}
word_set = {word.lower for word in words if word.strip()}

for word in words:
    word = word.lower()
    if word.strip():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


print(f"Словарь слов и количество их использования: {word_count}")
print("Количество уникальных слов в предложении: ", len(word_set))
