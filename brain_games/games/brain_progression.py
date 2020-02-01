import random

N = 10  # progression length
RULES = 'What number is missing in the progression?'


def make_round():
    a1 = random.randint(1, 10)  # value of the first member of the progression
    d = random.randint(1, 10)  # progression step
    an = a1 + (N - 1) * d  # last member of the progression
    hide = random.randint(0, N - 1)  # progression item to hide
    progression = list(map(str, range(a1, an + 1, d)))  # progression
    right_answer = str(progression[hide])
    progression[hide] = ".."
    return ' '.join(progression), right_answer
