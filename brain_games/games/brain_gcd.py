import random
import math


def logic():
    RULES = 'Find the greatest common divisor of given numbers.'
    number_1 = random.randint(1, 4)
    number_2 = random.randint(1, 4)
    right_answer = str(math.gcd(number_1, number_2))
    return RULES, '{} {}'.format(number_1, number_2), right_answer
