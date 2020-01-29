import random


def logic():
    N = 10  # длина прогрессии

    RULES = 'What number is missing in the progression?'
    a1 = random.randint(1, 10)  # значение первого члена прогрессии
    d = random.randint(1, 10)  # шаг прогрессии
    an = a1 + (N - 1) * d  # последний член прогрессии
    hide = random.randint(0, N - 1)  # номер скрываемого члена прогресии
    progression = list(map(str, range(a1, an + 1, d)))  # прогрессия
    right_answer = str(progression[hide])
    progression[hide] = ".."
    return RULES, ' '.join(progression), right_answer
