import random


def logic():
    rules = 'Answer "yes" if number even otherwise answer "no".'
    number = random.randint(1, 4)
    if number % 2 == 0:
        right_answer = 'yes'
    if number % 2 == 1:
        right_answer = 'no'
    return rules, '{}'.format(number), right_answer
