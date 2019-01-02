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
        self.client = cbpro.AuthenticatedClient(self.acc.getKey(), 
                                                self.acc.getSecret(),
                                                self.acc.getPassphrase())
        self.testConnection()

    def testConnection(self):
        accs = self.client.get_accounts()
        if len(accs) == 0:
            print('failed connection')

    def buy(self): 
        price = self.get_price(self.pair)
        ord = self.client.place_limit_order(self.pair, 'buy', price-self.bdi, self.amount)
        return ord['id']

    def sell(self):
        price = self.get_price(self.pair)
        ord = self.client.place_limit_order(self.pair, 'sell', price+self.profit, self.amount)
        return ord['id']

    def get_price(self, pair):
        tick = self.client.get_product_ticker(pair)
        return float(tick['price'])

    
if __name__ == "__main__":
    s = Selector('0.05', '0.05', 'BTC-USD', '0.05')
    s.get_price('BTC-USD')



