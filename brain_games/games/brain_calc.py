import random


def logic():
    rules = 'What is the result of the expression?'
    number_1 = random.randint(1, 4)
    number_2 = random.randint(1, 4)
    operation = random.choice(['+', '-', '*'])
    if operation == '+':
        right_answer = str(number_1 + number_2)
    if operation == '-':
        right_answer = str(number_1 - number_2)
    if operation == '*':
        right_answer = str(number_1 * number_2)
    return rules, '{}{}{}'.format(number_1, operation, number_2), right_answer
