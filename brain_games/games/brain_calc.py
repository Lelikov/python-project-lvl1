import random


def logic():
    RULES = 'What is the result of the expression?'
    number_1 = random.randint(1, 4)
    number_2 = random.randint(1, 4)
    operation = random.choice(['+', '-', '*'])
    if operation == '+':
        right_answer = str(number_1 + number_2)
    if operation == '-':
        right_answer = str(number_1 - number_2)
    if operation == '*':
        right_answer = str(number_1 * number_2)
    return RULES, '{}{}{}'.format(number_1, operation, number_2), right_answer
