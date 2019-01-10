from selector import Selector
import time

def main():
    s = Selector(0.05, 0.05, 'ETH-USD', 0.01)
    open_sells = []
    open_sells.insert(0, s.sell())
    open_buy = s.buy()
    trading = True
    
    while trading:
        try:
            while True:
                time.sleep(0.5)
                status = s.check_order_status(open_sells[-1], open_buy) #returns 'bought' or 'sold'
                print(status)
                if status == 'bought':
                    open_sells.insert(0, s.sell())
                    open_buy = s.buy()

                if status == 'sold':
                    open_sells.pop()
                    s.cancel()
                    open_buy = s.buy()
                    open_sells.insert(0, s.sell())
        except KeyboardInterrupt:
            print('Closed')
            break
        
        







if __name__ == "__main__":
    main()