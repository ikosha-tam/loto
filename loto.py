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
            # Вынимаем боченок из мешка
            pulled_barrel = loto_class.pull_barrel()
            size_bag = len(loto_class.bag)
            print()
            print(f'Новый боченок: {pulled_barrel} (осталось {size_bag})')
            # Выводим карточки на экран
            print_games_cards(title_1, title_2)

            # '1. Пользователь - Компьютер'
            if type_players == '1':
                # Ход игрока
                if num_in_card_gamer1 == 0:
                    print('Вы выиграли!!!. Зачеркнуты все цифры в карточке')
                    sys.exit()
                if num_in_card_gamer2 == 0:
                    print('Выиграл компьютер!!!. Зачеркнуты все цифры в карточке')
                    sys.exit()
                answer_player_1 = input('Зачеркнуть цифру? (y/n): ')
                if answer_player_1 == 'y' and pulled_barrel in gamer_1.card:
                    gamer_1.card[gamer_1.card.index(pulled_barrel)] = '><'
                    num_in_card_gamer1 -= 1
                    if pulled_barrel in gamer_1.card_line_1:
                        gamer_1.card_line_1[gamer_1.card_line_1.index(pulled_barrel)] = '><'
                    if pulled_barrel in gamer_1.card_line_2:
                        gamer_1.card_line_2[gamer_1.card_line_2.index(pulled_barrel)] = '><'
                    if pulled_barrel in gamer_1.card_line_3:
                        gamer_1.card_line_3[gamer_1.card_line_3.index(pulled_barrel)] = '><'
                elif answer_player_1 == 'n' and pulled_barrel in gamer_1.card:
                    print('Вы проиграли (число есть в карточке)')
                    sys.exit()
                elif answer_player_1 == 'y' and pulled_barrel not in gamer_1.card:
                    print('Вы проиграли (числа нет в карточке)')
                    sys.exit()
                elif answer_player_1 != 'n' and answer_player_1 != 'y':
                    print('Неверный ввод. Введите \"y\" или \"n\"')
                    sys.exit()

                # Ход компьютера
                if pulled_barrel in gamer_2.card:
                    gamer_2.card[gamer_2.card.index(pulled_barrel)] = '><'
                    num_in_card_gamer2 -= 1
                if pulled_barrel in gamer_2.card_line_1:
                    gamer_2.card_line_1[gamer_2.card_line_1.index(pulled_barrel)] = '><'
                if pulled_barrel in gamer_2.card_line_2:
                    gamer_2.card_line_2[gamer_2.card_line_2.index(pulled_barrel)] = '><'
                if pulled_barrel in gamer_2.card_line_3:
                    gamer_2.card_line_3[gamer_2.card_line_3.index(pulled_barrel)] = '><'

            # '2. Компьютер - Компьютер'
            if type_players == '2':
                if num_in_card_gamer1 == 0:
                    print('Выиграл компьютер 1!!!. Зачеркнуты все цифры в карточке')
                    sys.exit()
                if num_in_card_gamer2 == 0:
                    print('Выиграл компьютер 2!!!. Зачеркнуты все цифры в карточке')
                    sys.exit()

                # Ход компьютера 1
                # input()
                if pulled_barrel in gamer_1.card:
                    gamer_1.card[gamer_1.card.index(pulled_barrel)] = '><'
                    num_in_card_gamer1 -= 1
                if pulled_barrel in gamer_1.card_line_1:
                    gamer_1.card_line_1[gamer_1.card_line_1.index(pulled_barrel)] = '><'
                if pulled_barrel in gamer_1.card_line_2:
                    gamer_1.card_line_2[gamer_1.card_line_2.index(pulled_barrel)] = '><'
                if pulled_barrel in gamer_1.card_line_3:
                    gamer_1.card_line_3[gamer_1.card_line_3.index(pulled_barrel)] = '><'

                # Ход компьютера 2
                if pulled_barrel in gamer_2.card:
                    gamer_2.card[gamer_2.card.index(pulled_barrel)] = '><'
                    num_in_card_gamer2 -= 1
                if pulled_barrel in gamer_2.card_line_1:
                    gamer_2.card_line_1[gamer_2.card_line_1.index(pulled_barrel)] = '><'
                if pulled_barrel in gamer_2.card_line_2:
                    gamer_2.card_line_2[gamer_2.card_line_2.index(pulled_barrel)] = '><'
                if pulled_barrel in gamer_2.card_line_3:
                    gamer_2.card_line_3[gamer_2.card_line_3.index(pulled_barrel)] = '><'

            # '3. Пользователь - Пользователь'
            if type_players == '3':
                if num_in_card_gamer1 == 0:
                    print('Выиграл 1-й игрок!!!. Зачеркнуты все цифры в карточке')
                    sys.exit()
                if num_in_card_gamer2 == 0:
                    print('Выиграл 2-й игрок!!!. Зачеркнуты все цифры в карточке')
                    sys.exit()
                # Ход 1-го игрока
                answer_player_1 = input('Игрок-1, зачеркнуть цифру? (y/n): ')
                if answer_player_1 == 'y' and pulled_barrel in gamer_1.card:
                    gamer_1.card[gamer_1.card.index(pulled_barrel)] = '><'
                    num_in_card_gamer1 -= 1
                    if pulled_barrel in gamer_1.card_line_1:
                        gamer_1.card_line_1[gamer_1.card_line_1.index(pulled_barrel)] = '><'
                    if pulled_barrel in gamer_1.card_line_2:
                        gamer_1.card_line_2[gamer_1.card_line_2.index(pulled_barrel)] = '><'
                    if pulled_barrel in gamer_1.card_line_3:
                        gamer_1.card_line_3[gamer_1.card_line_3.index(pulled_barrel)] = '><'
                elif answer_player_1 == 'n' and pulled_barrel in gamer_1.card:
                    print('Игрок-1, вы проиграли (число есть в карточке)')
                    sys.exit()
                elif answer_player_1 == 'y' and pulled_barrel not in gamer_1.card:
                    print('Игрок-1, вы проиграли (числа нет в карточке)')
                    sys.exit()
                elif answer_player_1 != 'n' and answer_player_1 != 'y':
                    print('Неверный ввод. Введите \"y\" или \"n\"')
                    sys.exit()

                # Ход 2-го игрока
                answer_player_2 = input('Игрок-2, зачеркнуть цифру? (y/n): ')
                if answer_player_2 == 'y' and pulled_barrel in gamer_2.card:
                    gamer_2.card[gamer_2.card.index(pulled_barrel)] = '><'
                    num_in_card_gamer2 -= 1
                    if pulled_barrel in gamer_2.card_line_1:
                        gamer_2.card_line_1[gamer_2.card_line_1.index(pulled_barrel)] = '><'
                    if pulled_barrel in gamer_2.card_line_2:
                        gamer_2.card_line_2[gamer_2.card_line_2.index(pulled_barrel)] = '><'
                    if pulled_barrel in gamer_2.card_line_3:
                        gamer_2.card_line_3[gamer_2.card_line_3.index(pulled_barrel)] = '><'
                elif answer_player_2 == 'n' and pulled_barrel in gamer_2.card:
                    print('Игрок-2, вы проиграли (число есть в карточке)')
                    sys.exit()
                elif answer_player_2 == 'y' and pulled_barrel not in gamer_2.card:
                    print('Игрок-2, вы проиграли (числа нет в карточке)')
                    sys.exit()
                elif answer_player_2 != 'n' and answer_player_2 != 'y':
                    print('Неверный ввод. Введите \"y\" или \"n\"')
                    sys.exit()

    elif choise == '2':  # Выход
        sys.exit()
    else:
        print('Неверный пункт меню!')
