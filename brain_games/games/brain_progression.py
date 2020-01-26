import random
from brain_games.engine import greeting, welcome_user, \
    question, check_answer, congratulations


def progression():
    greeting()
    print('What number is missing in the progression?')
    name = welcome_user()
    for _ in range(1, 4):
        a1 = random.randint(1, 10)
        d = random.randint(1, 10)
        n = 10
        an = a1 + (n - 1) * d
        hide = random.randint(0, n - 1)
        progression = list(map(str, range(a1, an + 1, d)))
        right_answer = str(progression[hide])
        progression[hide] = ".."
        answer = question(' '.join(progression))
        if check_answer(right_answer, answer, name) is False:
            exit()
    return congratulations(name)
