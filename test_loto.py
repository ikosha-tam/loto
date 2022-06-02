import pytest

import loto_class
from loto_class import Loto

class TestLoto:

    def setUp(self):
        pass
        # self.gamer = Loto()

    def tearDown(self):
        pass
        # del self.gamer

    def test_init_bag(self):
        # gamer_test = Loto()
        loto_class.init_bag()
        assert loto_class.bag = [1,2,3,4,5,6,7]



