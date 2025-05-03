from random import randint

from brain_games import common


def get_nod(n1, n2):
    while n1 != n2:
        if n1 > n2:
            n1 -= n2
        else:
            n2 -= n1
    return n1


def gcd_game(name):
    points = 0
    for i in range(3):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        print('Question: ' + str(num1) + ' ' + str(num2))
        answer = input('Your answer: ')
        result = str(get_nod(num1, num2))
        check = common.check_answer(answer, result)
        if check:
            print('Correct!')
            points += 1
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{result}'.")
            print("Let's try again, " + name + "!")
            break
    if points == 3:
        print("Congratulations, " + name + "!")


def main():
    print("Welcome to the Brain Games!")
    name = common.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    gcd_game(name)


if __name__ == "__main__":
    main()
