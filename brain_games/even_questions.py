from random import randint
from prompt import string
from brain_games.cli import welcome_user


def questions():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = welcome_user()
    for _ in range(1, 4):
        number = randint(1, 100)
        print("Question: {}".format(number))
        answer = string("Your answer: ").lower()
        if answer == "yes" and not (number % 2):
            print("Correct!")
        elif answer == "no" and (number % 2):
            print("Correct!")
        else:
            wrong_answer = 'no' if (number % 2) else 'yes'
            print("'{}' is wrong answer ;(. Correct answer was \
                '{}'".format(answer, wrong_answer))
            return print("Let's try again, {}".format(name))
    return print("Congratulations, {}".format(name))
