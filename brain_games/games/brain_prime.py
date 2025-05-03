from random import randint

from brain_games import common


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


def prime_game(name):
    points = 0
    for i in range(3):
        num = randint(0, 100)
        is_prime_num = is_prime(num)
        print("Question: " + str(num))
        answer = input('Your answer: ')
        if is_prime_num:
            result = 'yes'
        else:
            result = 'no'
        check = common.check_answer(answer, result)
        if check:
            print('Correct!')
            points += 1
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{result}'.")
            print("Let's try again, " + name + "!")
            break
    if points == 3:
        print("Congratulations, " + name + "!")


def main():
    print("Welcome to the Brain Games!")
    name = common.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    prime_game(name)


if __name__ == "__main__":
    main()
