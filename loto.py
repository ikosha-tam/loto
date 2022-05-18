import loto_class
from loto_class import Loto
import sys

size_bag = 90  # Остаток боченков в мешке
num_in_card_gamer1 = 15  # число незачеркнутых цифр в карточке 1-го игрока
num_in_card_gamer2 = 15  # число незачеркнутых цифр в карточке 2-го игрока

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

        while size_bag > 0:  # Игра продолжается до пустого мешка
            if num_in_card_gamer1 == 0:
                print('Вы выиграли!!!. Зачеркнуты все цифры в карточке')
                sys.exit()
            # Вынимаем боченок из мешка
            pulled_barrel = loto_class.pull_barrel()
            size_bag = len(loto_class.bag)
            print()
            print('Новый боченок: ', pulled_barrel, ' (осталось )', size_bag)
            # Выводим карточки на экран
            print(num_in_card_gamer1, num_in_card_gamer2)
            print_games_cards(title_1, title_2)
            if type_players == '1':
                answer_player_1 = input('Зачеркнуть цифру? (y/n): ')
                if answer_player_1 == 'y' and pulled_barrel in gamer_1.card:
                    gamer_1.card[gamer_1.card.index(pulled_barrel)] = '><'
                    if pulled_barrel in gamer_1.card_line_1:
                        gamer_1.card_line_1[gamer_1.card_line_1.index(pulled_barrel)] = '><'
                    if pulled_barrel in gamer_1.card_line_2:
                        gamer_1.card_line_2[gamer_1.card_line_2.index(pulled_barrel)] = '><'
                    if pulled_barrel in gamer_1.card_line_3:
                        gamer_1.card_line_3[gamer_1.card_line_3.index(pulled_barrel)] = '><'
                    num_in_card_gamer1 -= 1
                # else:
                #     print('Вы проиграли (yy)')
                #     sys.exit()
                if answer_player_1 == 'n' and pulled_barrel in gamer_1.card:
                    print('Вы проиграли (ny)')
                    sys.exit()






    elif choise == '2':  # Выход
        sys.exit()
    else:
        print('Неверный пункт меню!')
