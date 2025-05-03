import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def check_answer(answer, result):
    if answer == result:
        return True
    else:
        return False