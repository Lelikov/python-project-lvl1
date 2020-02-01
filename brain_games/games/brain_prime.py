import random

RULES = (
    'Answer "yes" if given number is prime.'
    'Otherwise answer "no".'
)


def is_prime(number):
    '''
    Prime check
    :param number: Number for check
    :return: True if number is Prime, False number is composite
    '''
    if number % 2 == 0:
        return number == 2
    divider = 3
    while divider ** 2 <= number and number % divider != 0:
        divider += 2
    return divider ** 2 > number


def make_round():
    number = random.randint(1, 10)
    if is_prime(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return number, right_answer
