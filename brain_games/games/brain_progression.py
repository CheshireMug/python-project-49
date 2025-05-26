from random import randint

RULE = 'What number is missing in the progression?'


def generate_params():
    first = randint(0, 100)
    step = randint(1, 100)
    length = 10
    return first, step, length


def generate_answer(first, step, length):
    progression = [first + i * step for i in range(length)]
    hidden_index = randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    return progression, hidden_index, correct_answer


def generate_question(progression, hidden_index):
    question_list = list(map(str, progression))
    question_list[hidden_index] = '..'
    return ' '.join(question_list)


def generate_question_and_answer():
    first, step, length = generate_params()

    progression, hidden_index, correct_answer = generate_answer(
        first, step, length
    )

    question = generate_question(progression, hidden_index)

    return question, correct_answer
