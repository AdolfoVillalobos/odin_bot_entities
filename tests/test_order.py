import unittest


from odin_bot_entities.balances import Wallet, Coin
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

    def test_compute_remaining_amount_sufficient_funds(self):
        ticker_price = 50000  # 1 BTC = 50000 USDT

        wallet = Wallet(
            exchange="kraken",
            coins={"USDT": Coin(name="USDT", amount=4 * 50000)},
            sign=1.0,
        )
        remaining_amount = self.fake_order.calculate_remaining_position(
            pair_currency_factor=ticker_price, other_exchange_wallet=wallet
        )
        self.assertEqual(remaining_amount, 3 * 50000)

    def test_compute_remaining_amount_insufficient_funds(self):
        ticker_price = 50000  # 1 BTC = 50000 USDT

        wallet = Wallet(
            exchange="kraken",
            coins={"USDT": Coin(name="USDT", amount=1.5 * 50000)},
            sign=1.0,
        )
        remaining_amount = self.fake_order.calculate_remaining_position(
            pair_currency_factor=ticker_price, other_exchange_wallet=wallet
        )
        self.assertEqual(remaining_amount, 1.5 * 50000)
