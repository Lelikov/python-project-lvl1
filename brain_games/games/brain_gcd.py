import random

RULES = 'Find the greatest common divisor of given numbers.'


def gcd(number1, number2):
    if number2 == 0:
        return number1
    return gcd(number2, number1 % number2)


def make_round():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    right_answer = str(gcd(number1, number2))
    return '{} {}'.format(number1, number2), right_answer
