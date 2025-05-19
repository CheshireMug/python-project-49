from random import randint

from brain_games import common


RULE = 'Find the greatest common divisor of given numbers.'


def get_nod(n1, n2):
    while n1 != n2:
        if n1 > n2:
            n1 -= n2
        else:
            n2 -= n1
    return n1


def generate_question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(get_nod(num1, num2))
    return question, correct_answer
