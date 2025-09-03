import random

#declare the necessary variables
number_to_guess = random.randrange(1, 21)
number_of_tries = 5
count = 0

print(number_to_guess) #for debugging pueposes

while (count < number_of_tries):
    user_input = int(input("Guess the number [1 - 20]: "))
    number_of_tries -= 1

    if user_input == number_to_guess:
        print("You guessed the number: ", number_to_guess)
    elif number_of_tries == count:
        print("You ran out of tries!")
    elif user_input > 20:
        print("Number is out of range")
    else:
        print("Try again!")