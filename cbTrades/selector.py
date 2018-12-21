'''
class used to wrap AuthenticatedClient 
sets currency and buy/sell spreds
and price of orders
'''
import cbpro;
from auth_account.py import *

class Selector:

    def __init__(self, profit, bdi, pair, trade_amount): #profit, bdi == float

        # change TestClient to cbpro.AuthenticatedClient()
        # to trade real funds
        self.amount = trade_amount
        self.pair = pair
        self.profit = profit
        self.bdi = bdi
        self.account = Account()
        self.client = TestClient(account.getKey(), 
                                 account.getSecret(),
                                 account.getPassphrase())


    def buy(self, price):
        ord = self.client.place_limit_order(self.pair, 'buy', price-self.bdi, self.amount)
        return ord['id']

    def sell(self, price):
        ord = self.client.place_limit_order(self.pair, 'sell', price+self.profit, self.amount)
        return ord['id']

        
