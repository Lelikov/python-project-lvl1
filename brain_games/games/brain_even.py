import random

RULES = 'Answer "yes" if number even otherwise answer "no".'


def make_round():
    number = random.randint(1, 10)
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return str(number), right_answer
