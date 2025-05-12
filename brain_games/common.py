import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def check_answer(answer, result):
    if answer == result:
        return True
    else:
        return False


def check_points(points, name):
    if points == 3:
        print("Congratulations, " + name + "!")


def start_game(name, game_rule, generate_question_and_answer):
    print(game_rule)
    points = 0
    for i in range(3):
        question, correct_answer = generate_question_and_answer()
        print(f"Question: {question}")
        answer = input('Your answer: ')
        if check_answer(answer, correct_answer):
            print("Correct!")
            points += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    check_points(points, name)
