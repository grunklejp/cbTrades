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
        self.buy_to_cancel = None
        self.client = cbpro.AuthenticatedClient(self.acc.getKey(), 
                                                self.acc.getSecret(),
                                                self.acc.getPassphrase())
        self.testConnection()

    def testConnection(self):
        accs = self.client.get_accounts()
        if len(accs) == 0:
            print('failed connection')

    def buy(self): 
        price = self.get_price()
        new_price = price-self.bdi
        ord = self.client.place_limit_order(self.pair, 'buy', new_price, self.amount)
        
        try:
            print(ord['id'])
            self.buy_to_cancel = ord['id']
            return new_price
        except KeyError:
            print('order failed trying again')
            time.sleep(0.5)
            self.buy()
        
    def sell(self):
        price = self.get_price()
        new_price = price+self.profit
        ord = self.client.place_limit_order(self.pair, 'sell', new_price, self.amount)
        
        try:
            print(ord['id'])
            return new_price
        except KeyError:
            print('order failed trying again')
            time.sleep(0.5)
            self.sell()
    
    def cancel(self):
        self.client.cancel_order(self.buy_to_cancel)

    def get_price(self):
        tick = self.client.get_product_ticker(self.pair)
        try:
            return float(tick['price'])
        except KeyError:
            time.sleep(0.2)
            self.get_price()
    
    def check_order_status(self, sell_price, buy_price):
        current_price = self.get_price()
        # the current price rose past the sell price so order must have executed
        if current_price > sell_price:
            return 'sold'
        # current price sunk below the price to buy. buy must have executed
        if current_price < buy_price:
            return 'buy'
        return 'none'

         
def tester():
    acc = Account()
    s = cbpro.AuthenticatedClient(acc.getKey(), acc.getSecret(), acc.getPassphrase())
    check = s.place_limit_order('ETH-USD', 'sell', 130, 0.01)
    print(check)
    
if __name__ == "__main__":
    tester()
    



