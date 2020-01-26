import random
import math
from brain_games.engine import greeting, welcome_user, \
    question, check_answer, congratulations


def gcd():
    greeting()
    print('Find the greatest common divisor of given numbers.\n')
    name = welcome_user()
    for _ in range(1, 4):
        number_1 = random.randint(1, 4)
        number_2 = random.randint(1, 4)
        answer = question(number_1, number_2)
        right_answer = str(math.gcd(number_1, number_2))
        if check_answer(right_answer, answer, name) is False:
            exit()
    return congratulations(name)
