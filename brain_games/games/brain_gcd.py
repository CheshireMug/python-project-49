from random import randint

RULE = 'Find the greatest common divisor of given numbers.'


def get_nod(n1, n2):
    while n1 != n2:
        if n1 > n2:
            n1 -= n2
        else:
            n2 -= n1
    return n1


def generate_random_numbers():
    return randint(0, 100), randint(0, 100)


def generate_question(num1, num2):
    question = f"{num1} {num2}"
    correct_answer = str(get_nod(num1, num2))
    return question, correct_answer


def generate_question_and_answer():
    num1, num2 = generate_random_numbers()
    question, correct_answer = generate_question(num1, num2)
    return question, correct_answer
