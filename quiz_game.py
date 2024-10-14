print("Hello, Welcome to my computer quiz game!")

playing = input("Do you want to play the game?")

if playing != True:
    quit()

print("Great, Lets play the game")

response = input("What does your computer do?")
if response == "It works!":
    print("Correct answer!")
else:
    print("Sorry, incorrect answer!")
