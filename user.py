import random

max_number = input("Enter the maximum number for the guessing range: ")
if max_number.isdigit():
    max_number = int(max_number)
    
    if max_number <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    print("Please enter a valid number next time.")
    quit()
random_number = random.randint(0,max_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("Please type a number next time.")
        continue
    
    if user_guess == random_number:
        print("You got the number correct!")
        break
    
    elif user_guess > random_number:
        print("You were above the number!")
    
    else:
        print("You were below the number!")
print("You got it in", guesses,"guesses")