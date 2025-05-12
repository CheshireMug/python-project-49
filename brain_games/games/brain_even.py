from random import randint

from brain_games import common


def generate_even_question_and_answer():
    num = randint(0, 100)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return str(num), correct_answer


def main():
    name = common.welcome_user()
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    common.start_game(name, rule, generate_even_question_and_answer)


if __name__ == "__main__":
    main()
