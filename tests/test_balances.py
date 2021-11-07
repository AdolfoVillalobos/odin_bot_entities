import unittest
import time
from datetime import datetime


from odin_bot_entities.wallet import Wallet
from odin_bot_entities.balances import Balance


class TestWallets(unittest.TestCase):

    def test_get_balance_from_wallets(self):

        wallet1 = Wallet.parse_obj({
            "exchange": "orionX",
            "coins": {
                "BTC": {"name": "BTC", "amount": 2.0},
                "ETH": {"name": "ETH", "amount": 3.0},
            },
            "sign": 1,
            "time": time.time(),
            "date": datetime.utcnow()
        })

        wallet2 = Wallet.parse_obj({
            "exchange": "kraken",
            "coins": {
                "BTC": {"name": "BTC", "amount": 1.0},
                "ETH": {"name": "ETH", "amount": 4.0},
            },
            "sign": 1,
            "time": time.time(),
            "date": datetime.utcnow()
        })

        wallet3 = Wallet.parse_obj({
            "exchange": "orionx_loans",
            "coins": {
                "BTC": {"name": "BTC", "amount": 3.0},
                "ETH": {"name": "ETH", "amount": 7.0},
            },
            "sign": -1,
            "time": time.time(),
            "date": datetime.utcnow()
        })

        balance_coins = ["BTC", "ETH", "SOL"]
        wallets = [wallet1, wallet2, wallet3]
        precision_dict = {
            "ETH": 8,
            "BTC": 8,
            "SOL": 8
        }

        balance = Balance.from_wallets(
            balance_coins=balance_coins, wallets=wallets, precision_dict=precision_dict)

        self.assertEqual(balance.balance["BTC"]["Total"], 0.0)
        self.assertEqual(balance.balance["ETH"]["Total"], 0.0)
        self.assertEqual(balance.balance["SOL"]["Total"], 0.0)
