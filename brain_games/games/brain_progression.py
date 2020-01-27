import random
from brain_games.engine import greeting, welcome_user, \
    question, check_answer, congratulations


def progression():
    greeting('What number is missing in the progression?')
    name = welcome_user()
    for _ in range(1, 4):
        a1 = random.randint(1, 10)  # значение первого члена прогрессии
        d = random.randint(1, 10)  # шаг прогрессии
        N = 10  # длина прогрессии
        an = a1 + (N - 1) * d  # последний член прогрессии
        hide = random.randint(0, N - 1)  # номер скрываемого члена прогресии
        progression = list(map(str, range(a1, an + 1, d)))  # прогрессия
        right_answer = str(progression[hide])
        progression[hide] = ".."
        answer = question(' '.join(progression))
        if check_answer(right_answer, answer, name) is False:
            exit()
    return congratulations(name)
