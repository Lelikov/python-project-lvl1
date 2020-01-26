import random
from brain_games.engine import greeting, welcome_user, \
    question, check_answer, congratulations


def calc():
    greeting()
    print('What is the result of the expression?\n')
    name = welcome_user()
    for _ in range(1, 4):
        n1 = random.randint(1, 4)
        n2 = random.randint(1, 4)
        oper = random.choice(['+', '-', '*'])
        answer = question(n1, oper, n2)
        if oper == '+':
            right_answer = str(n1 + n2)
        if oper == '-':
            right_answer = str(n1 - n2)
        if oper == '*':
            right_answer = str(n1 * n2)
        if check_answer(right_answer, answer, name) is False:
            exit()
    return congratulations(name)
