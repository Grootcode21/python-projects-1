import random 

top_of_range = input("Please type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a positive number.")
        quit()

else:
    print("Error! You must type a number.")
    quit()

random_no = random.randint(0, top_of_range)

while True:
    user_guess = input(f"Guess a number between 0 and {top_of_range}: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_no:
            print("Congratulations! You guessed the correct number.")
            break
        elif user_guess < random_no:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
     



