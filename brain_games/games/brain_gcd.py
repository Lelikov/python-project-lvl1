import random, math


def logic():
    rules = 'Find the greatest common divisor of given numbers.'
    number_1 = random.randint(1, 4)
    number_2 = random.randint(1, 4)
    right_answer = str(math.gcd(number_1, number_2))
    return rules, '{} {}'.format(number_1, number_2), right_answer
