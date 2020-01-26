import prompt


def greeting():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}\n'.format(name))
    return name


def question(number_1, operation='', number_2=0):
    if operation == '':
        print('Question: {}'.format(number_1))
    else:
        print('Question: {} {} {}'.format(number_1, operation, number_2))
    return prompt.string('Your answer ')


def check_answer(right_answer, wrong_answer, name):
    if right_answer == wrong_answer:
        print('Correct! \n')
    else:
        print("\n'{}' is wrong answer ;(. Correct answer was '{}'\
        ".format(wrong_answer, right_answer))
        print("Let's try again, {}!".format(name))
        return False


def congratulations(name):
    print('Congratulations, {}!'.format(name))
