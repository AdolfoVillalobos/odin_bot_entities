import unittest
from datetime import datetime


from odin_bot_entities.coin import Coin


class TestCoins(unittest.TestCase):

    def test_add_two_coin_amounts(self):

        coin1 = Coin(name="BTC", amount=1.0)
        coin2 = Coin(name="BTC", amount=3.0)

        total = coin1+coin2
        self.assertEqual(total.name, "BTC")
        self.assertEqual(total.amount, 4.0)

    def test_multiply_coin_amount_by_scalar(self):

        coin1 = Coin(name="BTC", amount=2.5)
        coin2 = -10*coin1

        self.assertEqual(coin2.name, "BTC")
        self.assertEqual(coin2.amount, -25)

    def test_absolute_value_of_coin_amount(self):

        coin1 = Coin(name="BTC", amount=2.5)
        coin2 = -10*coin1
        coin3 = abs(coin2)

        self.assertEqual(coin3.name, "BTC")
        self.assertEqual(coin3.amount, 25)

    def test_coin_to_string(self):

        coin1 = Coin(name="BTC", amount=2.5)
        coin_str = str(coin1)

        self.assertTrue("BTC" in coin_str)
        self.assertTrue("2.5" in coin_str)
