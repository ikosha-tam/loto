import loto_class
from loto_class import Loto
import sys

size_bag = 90  # Остаток боченков в мешке

user = Loto()
computer = Loto()

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
            # Инициализируем мешок с боченками
            loto_class.init_bag()
            # Создаем карочки
            user.make_card()
            computer.make_card()
            # Выводим карточки на экран
            print(user.card)
            print(computer.card)
            print('{:-^26}'.format(' Ваша карточка '))
            user.print_card()
            for item in user.gamer_card:
                print(item)
            print('-' * 26)
            print('{:-^26}'.format(' Карточка компьютера '))
            computer.print_card()
            for item in computer.gamer_card:
                print(item)
            print('-' * 26)

            sys.exit()
        else:
            print('Неверный пункт меню!')
            sys.exit()



    elif choise == '2':  # Выход
        sys.exit()
    elif choise == '14':  # Вытащить боченок и вывести содержимое мешка
        pulled_barrel = loto_class.pull_barrel()
        size_bag = len(loto_class.bag)
        print('Новый боченок: ', pulled_barrel, ' (осталось )', size_bag)
        print(loto_class.bag)
    else:
        print('Неверный пункт меню!')
