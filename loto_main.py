# import random
import loto_moduls
from cards import Loto

human = Loto()




while True:
    print('*' * 50)

    print('1. Выбрать тип игроков')
    print('2. Играть')
    print('3. Выход')

    print('10. Создать карточку')
    print('11. Распечатать карточку')

    choise = input('Выберите пункт: ')
    if choise == '1':
        pass
    elif choise == '2':
        loto_moduls.init_bag()
    elif choise == '3':
        break

    elif choise == '10':
        human.make_card()
    elif choise == '11':
        print(human.card)

    else:
        print('Неверный пункт меню!')
