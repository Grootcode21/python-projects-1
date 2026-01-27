import random
import sys

def get_user_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer!")

def check_divisibility(number, divisor):
    return number % divisor == 0

def main():
    print("Welcome to the Divisibility Quiz!")
    print("I'll generate random numbers. Tell me if they're divisible by 2, 3, 4, and 5.")
    print("Enter 1 for 'yes' and 0 for 'no'.\n")
    
    score = 0
    questions_asked = 0

   
    while True:
        number = random.randint(1, 200)
        print(f"\nNumber: {number}")
        
        divisors = [2, 3, 4, 5]
        user_score = 0
        total_possible = len(divisors)
        
        for divisor in divisors:
            is_divisible = check_divisibility(number, divisor)
            correct_answer = 1 if is_divisible else 0
            
            user_answer = get_user_input(
                f"Is {number} divisible by {divisor}? (1 for yes, 0 for no): "
            )
            
            # Validate user input is 0 or 1
            while user_answer not in [0, 1]:
                print("Please enter either 0 (no) or 1 (yes)!")
                user_answer = get_user_input(
                    f"Is {number} divisible by {divisor}? (1 for yes, 0 for no): "
                )
            
            if user_answer == correct_answer:
                print(f"  ✓ Correct! {number} {'is' if is_divisible else 'is not'} divisible by {divisor}")
                user_score += 1
            else:
                print(f"  ✗ Incorrect! {number} {'is' if is_divisible else 'is not'} divisible by {divisor}")
        
        # Update overall score
        score += user_score
        questions_asked += 1
        
        print(f"\nFor this number: {user_score}/{total_possible} correct")
        print(f"Overall score: {score}/{questions_asked * total_possible}")
        
        # Ask if user wants to continue
        continue_game = input("\nDo you want to try another number? (y/n): ").lower()
        if continue_game not in ['y', 'yes']:
            print(f"\nThanks for playing! Final score: {score}/{questions_asked * total_possible}")
            break






def single_question_mode():
    print("\n=== Single Question Mode ===")
    number = random.randint(1, 200)
    print(f"\nNumber: {number}")
    
    divisors = [2, 3, 4, 5]
    answers = []
    
    for divisor in divisors:
        user_answer = get_user_input(
            f"Is {number} divisible by {divisor}? (1 for yes, 0 for no): "
        )
        while user_answer not in [0, 1]:
            print("Please enter either 0 (no) or 1 (yes)!")
            user_answer = get_user_input(
                f"Is {number} divisible by {divisor}? (1 for yes, 0 for no): "
            )
        answers.append((divisor, user_answer))
    
    # Check all answers
    print("\n" + "="*40)
    print(f"Results for number: {number}")
    print("="*40)
    
    correct_count = 0
    for divisor, user_answer in answers:
        is_divisible = check_divisibility(number, divisor)
        correct_answer = 1 if is_divisible else 0
        
        if user_answer == correct_answer:
            print(f"✓ Divisor {divisor}: Correct")
            correct_count += 1
        else:
            print(f"✗ Divisor {divisor}: Incorrect")
            print(f"  {number} {'is' if is_divisible else 'is not'} divisible by {divisor}")
    
    print(f"\nFinal score: {correct_count}/{len(divisors)}")
    
    print("\nDivisibility summary:")
    for divisor in divisors:
        result = "divisible" if number % divisor == 0 else "not divisible"
        print(f"  {number} is {result} by {divisor}")

if __name__ == "__main__":
    print("Choose Game Mode:")
    print("1: Multiple numbers (answer one divisor at a time)")
    print("2: Single number (answer all divisors at once)")
    
    mode = input("Enter mode (1 or 2): ").strip()
    
    if mode == "1":
        main()
    elif mode == "2":
        single_question_mode()
    else:
        print("Invalid choice. Running default mode...")
        main()