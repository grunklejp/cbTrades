'''

mimics functionality of AuthenticatedClient()
to test trading logic without using sandbox

'''

from cbpro import PublicClient
class TestClient:
    
    def __init__(self, key, secret, passphrase):
        self.balance = 1.5
        self.id = 1
        self.orders = []
        self.c = PublicClient()


    def place_limit_order(self, product_id, side, price, size):
        self.orders.append({'side': side, 
                            'price':price, 
                            'size': size, 
                            'id': self.id})
        self.id += 1
        return self.orders

    def get_price(self, product_id):
        d = self.c.get_product_ticker(product_id)
        return d['price']


if __name__ == "__main__":
    t = TestClient('asdf','sdfa','asdf')
    print(t.get_price('ETH-USD'))


