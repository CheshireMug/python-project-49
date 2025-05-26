from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_random_number():
    return randint(0, 100)


def generate_question_and_answer():
    num = generate_random_number()
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return str(num), correct_answer
