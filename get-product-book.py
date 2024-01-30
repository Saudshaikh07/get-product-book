import schedule
import time
import requests


def get_product_book():
    resp = requests.get('https://api.exchange.coinbase.com/products/BTC-USD/book')
    print(resp.json())


schedule.every(5).minutes.do(get_product_book)

while True:
    schedule.run_pending()
    time.sleep(1)
