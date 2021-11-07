import unittest
import time
from datetime import datetime


from odin_bot_entities.wallet import Wallet
from odin_bot_entities.balances import Balance


class TestWallets(unittest.TestCase):

    def setUp(self):
        self.orionx_wallet = Wallet.parse_obj({
            "exchange": "orionX",
            "coins": {
                "BTC": {"name": "BTC", "amount": 2.0},
                "ETH": {"name": "ETH", "amount": 3.0},
            },
            "sign": 1,
            "time": time.time(),
            "date": datetime.utcnow()
        })

        self.kraken_wallet = Wallet.parse_obj({
            "exchange": "kraken",
            "coins": {
                "BTC": {"name": "BTC", "amount": 1.0},
                "ETH": {"name": "ETH", "amount": 4.0},
            },
            "sign": 1,
            "time": time.time(),
            "date": datetime.utcnow()
        })

        self.orionx_loans_wallet = Wallet.parse_obj({
            "exchange": "orionx_loans",
            "coins": {
                "BTC": {"name": "BTC", "amount": 3.0},
                "ETH": {"name": "ETH", "amount": 7.0},
            },
            "sign": -1,
            "time": time.time(),
            "date": datetime.utcnow()
        })

        self.precision_dict = {
            "ETH": 8,
            "BTC": 8,
            "SOL": 8
        }

        self.balance_coins = ["BTC", "ETH", "SOL"]
        self.minimum_to_trade_dict = {
            "BTC": 0.01,
            "ETH": 0.03,
            "SOL": 0.5
        }

    def test_get_balance_from_wallets(self):

        wallets = [self.orionx_wallet,
                   self.kraken_wallet, self.orionx_loans_wallet]

        balance = Balance.from_wallets(
            balance_coins=self.balance_coins,
            wallets=wallets,
            precision_dict=self.precision_dict
        )

        self.assertEqual(balance.balance["BTC"]["Total"], 0.0)
        self.assertEqual(balance.balance["ETH"]["Total"], 0.0)
        self.assertEqual(balance.balance["SOL"]["Total"], 0.0)

    def test_wallets_are_balanced(self):
        wallets = [self.orionx_wallet,
                   self.kraken_wallet, self.orionx_loans_wallet]

        balance = Balance.from_wallets(
            balance_coins=self.balance_coins, wallets=wallets, precision_dict=self.precision_dict)

        unbalanced_coins = balance.is_unbalanced(
            balance_coins=self.balance_coins,
            minimum_to_trade_dict=self.minimum_to_trade_dict,
            rename_coin_dict={"BTC": "BTC", "ETH": "ETH", "SOL": "SOL"})

        self.assertEqual(unbalanced_coins, {})

    def test_wallets_are_unbalanced(self):
        wallets = [self.orionx_wallet, self.orionx_loans_wallet]

        balance = Balance.from_wallets(
            balance_coins=self.balance_coins, wallets=wallets, precision_dict=self.precision_dict)

        unbalanced_coins = balance.is_unbalanced(
            balance_coins=self.balance_coins,
            minimum_to_trade_dict=self.minimum_to_trade_dict,
            rename_coin_dict={"BTC": "BTC", "ETH": "ETH", "SOL": "SOL"})

        self.assertEqual(unbalanced_coins, {"BTC": -1.0, "ETH": -4.0})

    def test_wallets_are_unbalanced_but_cant_trade(self):
        wallets = [self.orionx_wallet, self.orionx_loans_wallet]
        self.minimum_to_trade_dict["BTC"] = 2.0

        balance = Balance.from_wallets(
            balance_coins=self.balance_coins, wallets=wallets, precision_dict=self.precision_dict)

        unbalanced_coins = balance.is_unbalanced(
            balance_coins=self.balance_coins,
            minimum_to_trade_dict=self.minimum_to_trade_dict,
            rename_coin_dict={"BTC": "BTC", "ETH": "ETH", "SOL": "SOL"})

        self.assertEqual(unbalanced_coins, {"ETH": -4.0})
