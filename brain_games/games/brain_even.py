from random import randint

from brain_games import common


def even_game(name):
    points = 0
    for i in range(3):
        num = randint(0, 100)
        print('Question: ' + str(num))
        if num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        answer = input('Your answer: ')
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
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even_game(name)


if __name__ == "__main__":
    main()
