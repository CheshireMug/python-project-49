import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def check_answer(answer, correct_answer, name):
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        exit()


def game_loop(name, game):
    for i in range(3):
        question, correct_answer = game.generate_question_and_answer()
        print(f"Question: {question}")
        answer = input('Your answer: ')
        check_answer(answer, correct_answer, name)
    print("Congratulations, " + name + "!")
    return


def start_game(game):
    name = welcome_user()
    print(game.RULE)
    game_loop(name, game)
