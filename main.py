import random as rand

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ValueError("Invalid")

def questions(operator):
    num1 = rand.randint(1, 20)
    num2 = rand.randint(1, 20)
    
    if operator == '+':
        answer = addition(num1, num2)
    elif operator == '-':
        answer = subtraction(num1, num2)
    elif operator == '*':
        answer = multiplication(num1, num2)
    elif operator == '/':
        answer = division(num1, num2)
    else:
        raise ValueError("Invalid operator")

    expression = f"{num1} {operator} {num2}"
    return expression, answer

def math_game():
    score = 0
    question_number = 5  
    
    print("Welcome to Math Quiz!")
    operator = input("Choose an operator (+, -, *, /): ")

    if operator not in ['+', '-', '*', '/']:
        print("Invalid operator. Please choose between +, -, *, or /.")
        return

    print(f"You chose '{operator}'")

    for _ in range(question_number):
        expression, answer = questions(operator)
        question = input(f"What is the answer to {expression}? ")
        try:
            question = float(question)
            if question == answer:
                print("You answered the correct answer!\n")
                score += 1
            else:
                print(f"You answered wrong! The correct answer is {answer}\n")
        except ValueError:
            print("Invalid input. Enter a number.\n")

    print(f"Congratulations! You got {score}/{question_number}")

if __name__ == "__main__":
    math_game()
