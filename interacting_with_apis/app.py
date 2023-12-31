import time
from libs.openExchange import OpenExchangeClient


APP_ID = "c8271892bb354e8398e354460df21a30"
'''
ENDPOINT = "https://openexchangerates.org/api/latest.json"
response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()["rates"]
'''
client = OpenExchangeClient(APP_ID)
usd_amount = 1000
start = time.time()
inr_amount = client.convert(usd_amount, "USD", "INR")
end = time.time()
print(end-start)
print(f"USD{usd_amount} is INR {inr_amount:.2f}")