'''
class used to wrap AuthenticatedClient 
sets currency and buy/sell spreds
and price of orders
'''
import cbpro
import time
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
        try:
            return ord['id']
        except KeyError:
            print('order failed trying again')
            time.sleep(0.5)
            self.buy()
        
    def sell(self):
        price = self.get_price(self.pair)
        ord = self.client.place_limit_order(self.pair, 'sell', price+self.profit, self.amount)
        
        try:
            print(ord['id'])
            return ord['id']
        except KeyError:
            print('order failed trying again')
            time.sleep(0.5)
            self.sell()
    
    def cancel(self, id):
        self.client.cancel_order(id)

    def get_price(self, pair):
        tick = self.client.get_product_ticker(pair)
        return float(tick['price'])
    
    def check_order_status(self, sell_id, buy_id):
        s = self.client.get_order(sell_id)
        b = self.client.get_order(buy_id)
        if s['status'] == 'done':
            return 'sold'
        if b['status'] == 'done':
            return 'buy'
        return 'none'

    
if __name__ == "__main__":
    s = Selector(0.05, 0.05, 'BTC-USD', 0.005)
    s.get_price('BTC-USD')
    id = s.sell()
    
