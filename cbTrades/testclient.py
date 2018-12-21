'''

mimics functionality of AuthenticatedClient()
to test trading logic without using sandbox

'''

class TestClient:
    
    def __init__(self, key, secret, passphrase):
        self.balance = 1.5
        self.id = 1
        self.orders = []


    def place_limit_order(self, product_id, side, price, size):
        self.orders.append({'side': side, 
                            'price':price, 
                            'size': size, 
                            'id': self.id})
        self.id += 1



