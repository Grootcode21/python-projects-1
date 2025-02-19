import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    guess = input("Problem #" + str(i +1) + ": " + expr + " = " )
    if guess == str(answer):
        break