import prompt

ROUNDS = 3


def greeting(intro):
    '''
    Displays the greeting and task of the game
    :param intro: Game task
    :return None
    '''
    print('Welcome to the Brain Games!')
    print(intro)
    print()


def welcome_user():
    '''
    Queries and returns the player’s name
    :return: None
    '''
    name = prompt.string('May I have your name? ')
    print('Hello, {}\n'.format(name))
    return name


def ask_question(question):
    '''
    Displays a question. Requests an answer
    :param question: Takes a string with a number value for the question
    :return: Response request
    '''
    print('Question: {}'.format(question))
    return prompt.string('Your answer ')


def congratulations(name):
    '''
    Displays the player’s congratulations on the successful
    completion of the game.
    :param name: Player name
    :return: None
    '''
    print('Congratulations, {}!'.format(name))


def run(game):
    '''
    Game engine
    :param game: Game module
    :return: None
    '''
    question, right_answer = game.make_round()
    greeting(game.RULES)
    name = welcome_user()
    for _ in range(ROUNDS):
        question, right_answer = game.make_round()
        answer = ask_question(question).lower()
        if answer == right_answer:
            print('Correct! \n')
            continue
        else:
            print("\n'{}' is wrong answer ;(. Correct answer was '{}'\
            ".format(answer, right_answer))
            print("Let's try again, {}!".format(name))
            return None
    congratulations(name)
