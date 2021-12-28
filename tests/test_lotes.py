import unittest
from datetime import datetime


from odin_bot_entities.lote import Lote


class TestLotes(unittest.TestCase):
    def setUp(self) -> None:

        self.lote = Lote(
            active=True,
            currency="BTC",
            origin_market="BTC/USDT",
            target_market="BTC/CLP",
            target_exchange="orionX",
            origin_exchange="binance",
            order_type="b",
            total_amount=100,
            collected=0.0,
            remaining=60,
            filled=40,
            time=186281653 + 10,
            date=datetime.utcnow(),
            order_ids=[],
            transaction_ids=[],
            trade_ids=[]
        )

    def test_is_full(self):

        self.lote.filled = 79
        self.assertFalse(self.lote.is_full())

        self.lote.filled = 81
        self.assertTrue(self.lote.is_full())

    def test_new_lote(self):

        new = Lote.new_lote(old_lote=self.lote)

        self.assertEqual(new.filled, 0.0)
        self.assertEqual(new.remaining, 100),
        self.assertEqual(new.total_amount, 100),
