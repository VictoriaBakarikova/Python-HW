user_input=input("Input numbers: ")
numbers=list(map(int, user_input.split()))

list_number=sorted(numbers, reverse=True)

print("The second largest number in list is", list_number[1])