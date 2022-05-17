import random

bag = []  # Список с номерами боченков в мешке
number_barrels = 90  # Число боченков в мешке


class Loto:
    def __init__(self):
        self.card = []
        self.gamer_card = []

    def make_card(self):
        """
        Создание новой карточки
        :return:
        """
        # Инициализация мешка с номерами боченков
        # init_bag()

        # Получаем 15 случайных чисел для игровой карточки
        self.card = random.sample(bag, k=15)
        self.card.sort()

        self.card_line_1 = random.sample(self.card, k=5)
        self.card_line_1.sort()

        # "Разбавляем" числа пробелами
        self.card_line_1.insert(random.randint(0, 4), '  ')
        self.card_line_1.insert(random.randint(0, 5), '  ')
        self.card_line_1.insert(random.randint(0, 6), '  ')
        self.card_line_1.insert(random.randint(0, 7), '  ')

        self.card_2_3 = list(set(self.card) - set(self.card_line_1))

        self.card_line_2 = random.sample(self.card_2_3, k=5)
        self.card_line_2.sort()
        self.card_line_2.insert(random.randint(0, 4), '  ')
        self.card_line_2.insert(random.randint(0, 5), '  ')
        self.card_line_2.insert(random.randint(0, 6), '  ')
        self.card_line_2.insert(random.randint(0, 7), '  ')

        self.card_line_3 = list(set(self.card_2_3) - set(self.card_line_2))
        self.card_line_3.sort()
        self.card_line_3.insert(random.randint(0, 4), '  ')
        self.card_line_3.insert(random.randint(0, 5), '  ')
        self.card_line_3.insert(random.randint(0, 6), '  ')
        self.card_line_3.insert(random.randint(0, 7), '  ')

    def print_card(self):
        self.line_1 = "{:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2}".format(*self.card_line_1)
        self.gamer_card.append(self.line_1)
        self.line_2 = "{:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2}".format(*self.card_line_2)
        self.gamer_card.append(self.line_2)
        self.line_3 = "{:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2}".format(*self.card_line_3)
        self.gamer_card.append(self.line_3)

        # print(self.gamer_card)

# Функции
def init_bag():
    """
    Функция инициализации мешка с номерами боченков
    :return:
    """
    bag.clear()
    for item in range(1, number_barrels + 1):
        bag.append(item)


def pull_barrel():
    """
    Вытаскивание случайного боченка из мешка с последующем его удалением из списка
    :return: Номер вытащенного боченка
    """
    barrel = random.choice(bag)
    bag.remove(barrel)
    return barrel

