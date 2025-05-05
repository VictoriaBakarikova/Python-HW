word_1=input("Input the word 1: ")
word_2=input("Input the word 2: ")

if sorted(word_1.lower()) == sorted(word_2.lower()):
    print("Annagramme")
else:
    print("These two words are't annagrammes")