from random import choice, randint

from brain_games import common


def check_question(name, points):
    operations = ['+', '-', '*']
    select_operation = choice(operations)
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    expression = f"{num1} {select_operation} {num2}"
    result = str(eval(expression))
    print('Question: ' + expression)
    answer = input('Your answer: ')
    check = common.check_answer(answer, result)
    if check:
        print('Correct!')
        points += 1
    else:
        print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{result}'.")
        print("Let's try again, " + name + "!")
    return points


def cycle(name, points):
    for i in range(3):
        points = check_question(name, points)
        if points < (i + 1):
            break
    return points


def calc_game(name):
    points = 0
    points = cycle(name, points)
    if points == 3:
        print("Congratulations, " + name + "!")


def main():
    print("Welcome to the Brain Games!")
    name = common.welcome_user()
    print('What is the result of the expression?')
    calc_game(name)


if __name__ == "__main__":
    main()
