from random import randint

# import prompt

from brain_games import common


# def welcome_user():
#     name = prompt.string('May I have your name? ')
#     print('Hello, ' + name + '!')
#     return name


def even_game(name):
    points = 0
    for i in range(3):
        num = randint(0, 100)
        print('Question: ' + str(num))
        answer = input('Your answer: ')
        if (num % 2 == 0) and answer == 'yes' or\
        (num % 2 != 0) and answer == 'no':
            print('Correct!')
            points += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + name + "!")
            break
    common.check_ponts(points, name)


def main():
    print("Welcome to the Brain Games!")
    name = common.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even_game(name)


if __name__ == "__main__":
    main()
