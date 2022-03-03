# get_crypto_prices

## Introduction
I use this to update crypto prices in spreadsheets instead of manually adding them. Yes, this is still sort of a manual process, but I can run multiple entries at once. I used to use the IMPORTXML command in GoogleSheets, but it sorta stopped working. I think Google products doesn't allow extensive web scraping anymore. On the other hand, the GOOGLEFINANCE command only works for BTC and ETH. Therefore, while waiting for other coins to work, I decided to use this script as a backup.

## Getting Started
Open get_crypto_prices.py, and change the coin_list array depending on your desired coins.

You can double check the ticker symbol from CoinGecko

```
python get_crypto_prices.py
```