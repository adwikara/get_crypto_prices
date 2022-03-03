import csv
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

# list of coins to monitor, CoinGecko API has limit 50 hits/minute
coin_list = [
    "bitcoin",
    "ethereum",
    "cardano",
    "solana",
    "matic-network",
    "polkadot",
    "chainlink"
]

# create csv file to store the prices
f = open('./crypto_updates.csv', 'w+')
writer = csv.writer(f)
writer.writerow(['token', 'price'])
data = []

# fetch the data and write to the csv file in the format [Symbol, Price]
for i in coin_list:
    data = [i, cg.get_price(ids=i, vs_currencies='usd')[i]['usd']]
    writer.writerow(data)
