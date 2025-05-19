from random import randint

from brain_games import common


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    num = randint(0, 100)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return str(num), correct_answer
