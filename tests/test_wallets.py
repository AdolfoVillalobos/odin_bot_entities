import unittest
import time
from datetime import datetime


from odin_bot_entities.wallet import Wallet


class TestWallets(unittest.TestCase):

    def test_get_wallet_item(self):

        wallet = Wallet.parse_obj({
            "exchange": "orionX",
            "coins": {
                "BTC": {"name": "BTC", "amount": 1.0},
                "ETH": {"name": "ETH", "amount": 3.0},
            },
            "sign": 1,
            "time": time.time(),
            "date": datetime.utcnow()
        })

        self.assertEqual(wallet["BTC"].name, "BTC")
        self.assertEqual(wallet["BTC"].amount, 1.0)
        self.assertEqual(wallet["ETH"].name, "ETH")
        self.assertEqual(wallet["ETH"].amount, 3.0)
        self.assertEqual(wallet["SOL"].name, "SOL")
        self.assertEqual(wallet["SOL"].amount, 0.0)
