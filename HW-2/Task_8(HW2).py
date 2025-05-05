import random
random_number=random.randint(1, 100)
print("I thought a number, guess what it is!")


while True:
    user_guess=int(input("Input the number: "))
    if user_guess > random_number:
        print ("Less!")
    elif user_guess < random_number:
        print("More")
    else:
        print("You're guess")
        break

