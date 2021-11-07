import unittest
from datetime import datetime


from odin_bot_entities.trades import Order, Transaction


class TestOrders(unittest.TestCase):
    def setUp(self) -> None:
        self.usd_observed = 782
        self.true_currency_utility = 0
        self.true_pair_currency_utility = 0.1

        self.fake_transaction = Transaction(
            id="test-transaction1",
            currency_name="BTC",
            pair_currency_name="CLP",
            market="BTC/CLP",
            exchange="orionX",
            time=186281653 + 10,
            type="buy",
            currency_value=1,
            fee=0.1,
            pair_currency_value=1000,
        )

        self.fake_transaction2 = Transaction(
            id="test-transaction2",
            currency_name="BTC",
            pair_currency_name="CLP",
            market="BTC/CLP",
            exchange="orionX",
            time=186281653 + 15,
            type="buy",
            currency_value=2,
            fee=0.1,
            pair_currency_value=2000,
        )

        self.fake_order = Order(
            id="test-order",
            amount=6.0,
            status="open",
            type="b",
            market="BTC/CLP",
            exchange="orionX",
            transactions=[self.fake_transaction, self.fake_transaction2],
        )

    def test_compute_balance(self):

        self.assertEqual(self.fake_order.currency_balance, 3)
        self.assertEqual(self.fake_order.pair_currency_balance, 3000)
