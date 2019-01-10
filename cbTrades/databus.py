from cbpro import WebsocketClient
from selector import Selector
import time
import json




class ClientFeed(WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        # s = (profit in usd, bdi in usd, pair, ammount of crypto to trade)
        self.s = Selector(0.05, 0.05, 'ETH-USD', 0.01)
        self.products = [self.s.pair]
        self.open_sells = []
        self.open_buy = self.s.buy()
        self.open_sells.insert(0, self.s.sell())

    def on_message(self, msg):

        ''' msg 
        {
            "order_id": "e6fc6c86-08f2-4740-8402-b0cb654288c4",
            "price": "115.95000000",
            "product_id": "ETH-USD",
            "remaining_size": "30.80477473",
            "sequence": 6043317961,
            "side": "buy",
            "time": "2018-12-27T21:25:37.119000Z",
            "type": "open"
        }
        '''

        ''' trade logic'''

        if msg['type'] == 'done' and msg['reason'] == 'filled':
            #if account buys, places new sell target, places new buy
            if msg['order_id'] == self.open_buy:
                self.open_sells.insert(0, self.s.sell())
                self.open_buy = self.s.buy()
                
            #if account sells cancel open buy and replace new buy and sell
            if msg['order_id'] == self.open_sells[-1]:
                self.open_sells.pop()
                self.s.cancel(self.open_buy)
                self.open_buy = self.s.buy()
                self.open_sells.insert(0, self.s.sell())


    def on_close(self):
        print("-- Goodbye! --")

if __name__ == "__main__":
    client = ClientFeed()
    client.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        wsClient.close()

    if wsClient.error:
        sys.exit(1)
    else:
        sys.exit(0)

    