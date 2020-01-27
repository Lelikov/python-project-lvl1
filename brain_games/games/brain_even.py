import random
from brain_games.engine import greeting, welcome_user, \
    question, check_answer, congratulations


def even():
    greeting()
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = welcome_user()
    for _ in range(1, 4):
        number_1 = random.randint(1, 4)
        answer = question(number_1).lower()
        if number_1 % 2 == 0:
            right_answer = 'yes'
        if number_1 % 2 == 1:
            right_answer = 'no'
        if check_answer(right_answer, answer, name) is False:
            exit()
    return congratulations(name)