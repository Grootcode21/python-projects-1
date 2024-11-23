name = input("Please enter you name: ")
print("Hello",name, "Welcome to my adventure game!")

answer = input("You have come to an end of a dirt road. Would like to go left or right?").lower()

if answer == "left":
    answer == input("you come to a river. You can walk around it or swim accross it.")

    if answer == "walk":
        answer = "you find a hidden cave. You can enter or leave."

        if answer == "enter":
            answer = "you get bitten by a venomous snake and you lose the game."
        
        elif answer == "leave":
            answer = "you come across a lonely pathway.You can go foward or go back"

        else:
            print('This is not a valid option')
                
    elif answer == "swim":
        answer = "you drown and die.You lose the game"

    else:
        print('This is not a valid option')
    
elif answer == "right":
    answer == input("you come to an end. You can go left or quit.")


else:
    print('This is not a valid answer. You lose')

    