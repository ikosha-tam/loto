import random
from card_loto import Loto

human = Loto()
bag = []
# Инициализация мешка
for item in range(1, 91):
    bag.append(item)
print(bag)
for i in range(10):
    random_number = random.choice(bag)
    print(random_number, len(random_number))
    random_number.remove(random_number)
    input()

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
        pass
    elif choise == '3':
        break

    elif choise == '10':
        human.make_card()
    elif choise == '11':
        print(human.card)

    else:
        print('Неверный пункт меню!')
