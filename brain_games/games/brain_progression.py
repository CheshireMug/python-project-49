from random import randint

from brain_games import common


def gen_arr():
    first = randint(0, 100)
    arr = [first]
    
    step = randint(1, 100)
    for _ in range(9):
        next_element = arr[-1] + step
        arr.append(next_element)

    return arr


def hid_arr(arr):
    hidden_arr = list(map(str, arr))
    hidden_el = randint(0, 9)
    hidden_arr[hidden_el] = '..'
    return hidden_arr, hidden_el


def progression_game(name):
    points = 0
    for i in range(3):
        arr = gen_arr()
        hidden_arr, hidden_el = hid_arr(arr)
        print("Question: " + f"{' '.join(hidden_arr)}")
        answer = input('Your answer: ')
        result = str(arr[hidden_el])
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
    print('What number is missing in the progression?')
    progression_game(name)


if __name__ == "__main__":
    main()
