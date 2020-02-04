import random
from operator import add, sub, mul

RULES = 'What is the result of the expression?'
OPERATIONS = [('+', add), ('-', sub), ('*', mul)]


def make_round():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    sign, operation = random.choice(OPERATIONS)
    right_answer = str(operation(number1, number2))
    return '{}{}{}'.format(number1, sign, number2), right_answer
