from random import choice, randint

from brain_games import common


RULE = 'What is the result of the expression?'


def generate_question_and_answer():
    operations = ['+', '-', '*']
    select_operation = choice(operations)
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    expression = f"{num1} {select_operation} {num2}"
    result = str(eval(expression))
    return expression, result
