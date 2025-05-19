from random import randint

from brain_games import common


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def generate_question_and_answer():
    num = randint(0, 100)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return str(num), correct_answer
