class Loto:
    def __init__(self):
        self.card = {
            1: [],
            2: [],
            3: []
        }

    def make_card(self):
        """
        Создание новой карточки
        :return:
        """
        self.card = {
            1: [1, 2, 3, 4, 5],
            2: [6, 7, 8, 9, 10],
            3: [11, 12, 13, 14, 15]
        }

    def print_card(self):
        """
        Вывести карточку на экран
        :return:
        """
        return self.card
