import random 

top_of_range = input("Please type a number: ")

if not top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a positive number.")
        quit()

else:
    print("Error! You must type a number.")
    quit()

random_no = random.randint(0, top_of_range)
print("The random number is:", random_no)




