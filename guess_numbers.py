import random 

top_of_range = input("Please type a number: ")

if not top_of_range.isdigit():
    print("Error: You must enter a number.")

while True:
    try:
        number = random.randint(1, int(top_of_range))
        break
    except ValueError:
        print("Error: You must enter a valid number.")