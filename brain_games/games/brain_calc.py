from random import choice, randint

RULE = 'What is the result of the expression?'


def generate_operation():
    operations = ['+', '-', '*']
    select_operation = choice(operations)
    return select_operation


def generate_random_numbers():
    return randint(0, 100), randint(0, 100)


def generate_expression(num1, num2, select_operation):
    expression = f"{num1} {select_operation} {num2}"
    result = str(eval(expression))
    return expression, result


def generate_question_and_answer():
    select_operation = generate_operation()
    num1, num2 = generate_random_numbers()
    expression, result = generate_expression(num1, num2, select_operation)
    return expression, result
