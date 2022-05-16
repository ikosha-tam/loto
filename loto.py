import loto_class
from loto_class import Loto

size_bag = 90   # Остаток боченков в мешке

human = Loto()

while True:
    print('*' * 50)

    print('1. Выбрать тип игроков')
    print('2. Играть')
    print('3. Выход')
    print()
    print('10. Создать карточку')
    print('11. Распечатать карточку')
    print()
    print('12. Инициализация мешка')
    print('13. Вывести содержимое мешка')
    print('14. Вытащить боченок и вывести содержимое мешка')

    choise = input('Выберите пункт: ')
    if choise == '1':  # Выбрать тип игроков
        pass
    elif choise == '2':  # Играть
        pass
    elif choise == '3':  # Выход
        break

    elif choise == '10':  # Создать карточку
        human.make_card()
        print(human.card)
    elif choise == '11':  # Распечатать карточку
        print(human.card)
        print(human.card_line_1)
        print(human.card_line_2)
        print(human.card_line_3)
    elif choise == '12':  # Инициализация мешка
        loto_class.init_bag()
    elif choise == '13':  # Вывести содержимое мешка
        print(loto_class.bag)
    elif choise == '14':  # Вытащить боченок и вывести содержимое мешка
        pulled_barrel = loto_class.pull_barrel()
        size_bag = len(loto_class.bag)
        print('Новый боченок: ', pulled_barrel, ' (осталось )', size_bag)
        print(loto_class.bag)
    else:
        print('Неверный пункт меню!')
