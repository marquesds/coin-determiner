from django.test import TestCase
from coin_determiner.determiner.models import Coin


class TestCoin(TestCase):
    def setUp(self):
        self.coin = Coin()

    def test_least_number_of_coins(self):
        list = [6, 16, 23]
        expected_result = [2, 2, 3]
        index = 0
        for element in list:
            self.assertEquals(self.coin.coinDeterminer(element), expected_result[index])
            index += 1
