import prompt


def greeting(intro):
    '''
    Выводит приветствие и задачу игры
    :param intro: Задача игры
    :return None
    '''
    print('Welcome to the Brain Games!')
    print(intro, '\n')


def welcome_user():
    '''
    Запрашивает и возвращает имя игрока
    :return: None
    '''
    name = prompt.string('May I have your name? ')
    print('Hello, {}\n'.format(name))
    return name


def question(number_1, number_2=None, operation=' '):
    '''
    Выводит строку с вопросом. Запрашивает ответ
    :param number_1: Принимает строку со значением числа для вопроса
    :param number_2: Принимает строку со значением второго числа,
            если в вопросе содержится какая либо операция с числами
    :param operation: Принимает строку со значением математического
            оператора
    :return: Строка с запросом ответа
    '''
    if number_2 is None:
        print('Question: {}'.format(number_1))
    else:
        print('Question: {}{}{}'.format(number_1, operation, number_2))
    return prompt.string('Your answer ')


def check_answer(right_answer, answer, name):
    '''
    Сравнивает ответ данный игроком с правильным ответом
    В случае правильного ответа выводит подтверждение.
    В случае неправильного ответа выводит правильный ответ и
    сообщение об окончании игры
    :param right_answer: Правильный ответ
    :param answer: Ответ игрока
    :param name: Имя игрока
    :return: Возвращает False при неправильном ответе
    '''
    if answer == right_answer:
        print('Correct! \n')
    else:
        print("\n'{}' is wrong answer ;(. Correct answer was '{}'\
        ".format(answer, right_answer))
        print("Let's try again, {}!".format(name))
        return False


def congratulations(name):
    '''
    Выводит поздравление игрока об успешном окончании игры
    :param name: Имя игрока
    :return: None
    '''
    print('Congratulations, {}!'.format(name))


def isPrime(number):
    '''
    Проверка на простое число
    :param number: Число для проверка
    :return: True если число простое, False если число составное
    '''
    if number % 2 == 0:
        return number == 2  # если число четное, то возвращаем False (кроме 2)
    divider = 3
    while divider ** 2 <= number and number % divider != 0:
        divider += 2
    return divider ** 2 > number
