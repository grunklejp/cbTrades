from cbpro import WebsocketClient
from selector import Selector
import time
import json




class ClientFeed(WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.sel = Selector(0.05, 0.05, 'ETH-USD', 0.1)
        self.products = [self.sel.pair]
        self.b = self.sel.buy()
        self.s = self.sel.sell()

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

        if msg['type'] == 'done':
            if msg['reason'] == 'filled':
                print(json.dumps(msg, indent=4, sort_keys=True))

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

    