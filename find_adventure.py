name = input("Please enter you name: ")
print("Hello",name, "Welcome to my adventure game!")

answer = input("You have come to an end of a dirt road. Would like to go left or right?").lower()

if answer == "left":
    answer == input("you come to a river. You can walk around it or swim accross it.")

    if answer == "walk":
        answer = "you find a hidden cave. You can enter or leave."
        
    elif answer == "swim":
        answer = "you drown and die."

    else:
        print('This is not a valid option')
    
elif answer == "right":
    print()

else:
    print('This is not a valid answer. You lose')

    