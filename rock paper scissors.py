import random 

user_wins = 0
computer_wins = 0

choices = ['rock', 'paper', 'scissors']

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    if user_choice == 'q':
        quit()

    if user_choice not in choices:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue

    random_no = random.randint(0,2)
# rock: 0, paper:1, scissors:2

    computer_choice = choices[random_no]
    print("Computer chose:", computer_choice + ".")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        user_wins += 1
    else:
        print("You lost. Computer wins!")
        computer_wins += 1



