from random import randint
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def calc_game(name):
    points = 0
    for i in range(3):
        num1 = randint(0, 100)
        num2 = randint(0, 100)
        operation = randint(0, 2)
        if operation == 0:
            print('Question: ' + str(num1) + ' + ' + str(num2))
            answer = int(input('Your answer: '))
            if answer == (num1 + num2):
                print('Correct!')
                points += 1
            else:
                print(
                    f"'{answer}' is is wrong answer ;(. \
Correct answer was '{num1 + num2}'."
                    )
                print("Let's try again, " + name + "!")
                break
        elif operation == 1:
            print('Question: ' + str(num1) + ' - ' + str(num2))
            answer = int(input('Your answer: '))
            if answer == (num1 - num2):
                print('Correct!')
                points += 1
            else:
                print(
                    f"'{answer}' is is wrong answer ;(. \
Correct answer was '{num1 - num2}'."
                    )
                print("Let's try again, " + name + "!")
                break
        elif operation == 2:
            print('Question: ' + str(num1) + ' * ' + str(num2))
            answer = int(input('Your answer: '))
            if answer == (num1 * num2):
                print('Correct!')
                points += 1
            else:
                print(
                    f"'{answer}' is is wrong answer ;(. \
Correct answer was '{num1 * num2}'."
                    )
                print("Let's try again, " + name + "!")
                break
    if points == 3:
        print("Congratulations, " + name + "!")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('What is the result of the expression?')
    calc_game(name)


if __name__ == "__main__":
    main()
