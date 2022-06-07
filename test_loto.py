import pytest
import loto_class
from loto_class import Loto


class TestLoto:
    def test_init_bag(self):
        test_bag = []
        for item in range(1, 91):
            test_bag.append(item)
        loto_class.init_bag()
        assert loto_class.bag == test_bag

    def test_pull_barrel(self):
        test_barrel = loto_class.pull_barrel()
        assert test_barrel in range(1, 91)

    def test_make_card(self):
        test_gamer = Loto()
        test_gamer.make_card()
        assert len(test_gamer.card) == 15