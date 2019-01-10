# Market Maker bot for Coinbase Pro
# Uses /coinbase-pro by danpaquin

To run:
create file named auth.py with these contents:

class Account:
     
    def __init__(self):
        self.key = ''
        self.secret = ''
        self.passphrase = ''

    def getKey(self):
        return self.key

    def getSecret(self):
        return self.secret

    def getPassphrase(self):
        return self.passphrase

set coinbase pro api key, secret, and passphrase in auth.py



set Selector parameters in on_open in databus.py



