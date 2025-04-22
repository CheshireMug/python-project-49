from random import randint

import prompt


def get_nod(n1, n2):
    while n1 != n2:
        if n1 > n2:
            n1 -= n2
        else:
            n2 -= n1
    return n1


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def gcd_game(name):
    points = 0
    for i in range(3):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        print('Question: ' + str(num1) + ' ' + str(num2))
        answer = int(input('Your answer: '))
        if answer == (get_nod(num1, num2)):
            print('Correct!')
            points += 1
        else:
            print(
                    f"'{answer}' is is wrong answer ;(. \
Correct answer was '{get_nod(num1, num2)}'."
                    )
            print("Let's try again, " + name + "!")
            break
    if points == 3:
        print("Congratulations, " + name + "!")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    gcd_game(name)


if __name__ == "__main__":
    main()
