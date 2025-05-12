from random import randint

from brain_games import common


def generate_progression_question_and_answer():
    first = randint(0, 100)
    step = randint(1, 100)
    length = 10

    progression = [first + i * step for i in range(length)]
    hidden_index = randint(0, length - 1)
    correct_answer = str(progression[hidden_index])

    question_list = list(map(str, progression))
    question_list[hidden_index] = '..'
    question = ' '.join(question_list)

    return question, correct_answer


def main():
    name = common.welcome_user()
    rule = 'What number is missing in the progression?'
    common.start_game(name, rule, generate_progression_question_and_answer)


if __name__ == "__main__":
    main()
