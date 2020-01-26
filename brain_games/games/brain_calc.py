import random
from brain_games.engine import greeting, welcome_user, \
    question, check_answer, congratulations


def calc():
    greeting()
    print('What is the result of the expression?\n')
    name = welcome_user()
    for _ in range(1, 4):
        number_1 = random.randint(1, 4)
        number_2 = random.randint(1, 4)
        operation = random.choice(['+', '-', '*'])
        answer = question(number_1, number_2, operation)
        if operation == '+':
            right_answer = str(number_1 + number_2)
        if operation == '-':
            right_answer = str(number_1 - number_2)
        if operation == '*':
            right_answer = str(number_1 * number_2)
        if check_answer(right_answer, answer, name) is False:
            exit()
    return congratulations(name)
