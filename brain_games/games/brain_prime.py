
import random
from brain_games.engine import greeting, welcome_user, \
    question, check_answer, congratulations, isPrime


def prime():
    greeting('Answer "yes" if given number is prime. \
Otherwise answer "no".')
    name = welcome_user()
    for _ in range(1, 4):
        number = random.randint(1, 100)
        answer = question(number).lower()
        if isPrime(number):
            right_answer = 'yes'
        else:
            right_answer = 'no'
        if check_answer(right_answer, answer, name) is False:
            exit()
    return congratulations(name)
