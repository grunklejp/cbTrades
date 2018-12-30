'''
class used to wrap AuthenticatedClient 
sets currency and buy/sell spreds
and price of orders
'''
import cbpro
from testclient import TestClient
from auth import Account

class Selector:

    def __init__(self, profit, bdi, pair, trade_amount): #profit, bdi == float

        # change TestClient to cbpro.AuthenticatedClient()
        # to trade real funds
        self.amount = trade_amount
        self.pair = pair
        self.profit = profit
        self.bdi = bdi
        self.acc = Account()
        self.client = TestClient(self.acc.getKey(), 
                                 self.acc.getSecret(),
                                 self.acc.getPassphrase())


    def buy(self):
        price = float(self.client.get_price(self.pair))
        ord = self.client.place_limit_order(self.pair, 'buy', price-self.bdi, self.amount)
        return ord[-1]

    def sell(self):
        price = float(self.client.get_price(self.pair))
        ord = self.client.place_limit_order(self.pair, 'sell', price+self.profit, self.amount)
        return ord[-1]

        
