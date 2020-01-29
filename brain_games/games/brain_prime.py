import random
from brain_games.engine import is_prime


def logic():
    RULES = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'
    number = random.randint(1, 100)
    if is_prime(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return RULES, '{}'.format(number), right_answer
