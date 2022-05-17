import loto_class
from loto_class import Loto
import sys

size_bag = 90  # Остаток боченков в мешке

gamer_1 = Loto()
gamer_2 = Loto()

def print_games_cards(title_1, title_2):
    '''
    Выводим карточки на экран
    :param title_1: Заголовок 1-й карточки
    :param title_2: Заголовок 2-й карточки
    :return:
    '''
    print(gamer_1.card)
    print(gamer_2.card)
    print('{:-^26}'.format(title_1))
    gamer_1.print_card()
    for item in gamer_1.gamer_card:
        print(item)
    print('-' * 26)
    print('{:-^26}'.format(title_2))
    gamer_2.print_card()
    for item in gamer_2.gamer_card:
        print(item)
    print('-' * 26)


while True:
    print('1. Играть')
    print('2. Выход')
    print()
    print('14. Вытащить боченок и вывести содержимое мешка')

    choise = input('Выберите пункт: ')
    if choise == '1':  # Играть
        print('Выберете тип игроков:')
        print('1. Пользователь - Компьютер')
        print('2. Компьютер - Компьютер')
        print('3. Пользователь - Пользователь')
        type_players = input('=> ')

        if type_players == '1':
            title_1 = ' Ваша карточка '
            title_2 = ' Карточка компьютера '
        elif type_players == '2':
            title_1 = ' Карточка компьютера-1 '
            title_2 = ' Карточка компьютера-2 '
        elif type_players == '3':
            title_1 = ' Ваша карточка '
            title_2 = ' Карточка игрока-2 '
        else:
            print('Неверный пункт меню!')
            sys.exit()

        # Инициализируем мешок с боченками
        loto_class.init_bag()
        # Создаем карточки
        gamer_1.make_card()
        gamer_2.make_card()
        # Выводим карточки на экран
        print_games_cards(title_1, title_2)
        break


    elif choise == '2':  # Выход
        sys.exit()
    elif choise == '14':  # Вытащить боченок и вывести содержимое мешка
        pulled_barrel = loto_class.pull_barrel()
        size_bag = len(loto_class.bag)
        print('Новый боченок: ', pulled_barrel, ' (осталось )', size_bag)
        print(loto_class.bag)
    else:
        print('Неверный пункт меню!')
