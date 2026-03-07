# '''
# Endpoint: https://paper-api.alpaca.markets/v2
# Key: PKM6SICFKQ7P6FKSXYXVP2OAG4
# Secret: 7XFKjFipcTKhLmthTb7vgoTV75QwWu1dCsqBo3SVj152
# '''

# from alpaca.data.historical import CryptoHistoricalDataClient
# from alpaca.data.requests import CryptoBarsRequest
# from alpaca.data.timeframe import TimeFrame
# import datetime

# # No keys required for crypto data
# client = CryptoHistoricalDataClient()

# # Creating request object
# request_params = CryptoBarsRequest(
#   symbol_or_symbols=["BTC/USD"],
#   timeframe=TimeFrame.Day,
#   start=datetime.datetime(2026, 3, 1),
#   end=datetime.datetime(2026, 3, 7)
# )

# # Retrieve daily bars for Bitcoin in a DataFrame and printing it
# btc_bars = client.get_crypto_bars(request_params)

# # Convert to dataframe
# btc_bars.df

# timestamps = btc_bars["BTC/USD"]

# ASSETS #

# from alpaca.trading.client import TradingClient
# from alpaca.trading.requests import GetAssetsRequest
# from alpaca.trading.enums import AssetClass

# trading_client = TradingClient('PKM6SICFKQ7P6FKSXYXVP2OAG4', '7XFKjFipcTKhLmthTb7vgoTV75QwWu1dCsqBo3SVj152')

# # search for US equities
# search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)

# assets = trading_client.get_all_assets(search_params)
# # print(assets)

# # search for AAPL
# aapl_asset = trading_client.get_asset('AAPL')

# if aapl_asset.tradable:
#     print(aapl_asset)

import yfinance as yf

userinput = input('Enter the asset to analyze: ')

ticker = yf.Ticker(f"{userinput}")
info = ticker.info

# print(info)

marketcap = f"{info["marketCap"]:,}"
print(f"Asset Entered: {info["displayName"]}")
print(f"Market Cap: ${marketcap}")
print(f"Dividend Yield: {info["dividendYield"]}%")
print(f"P/E Ratio: {info["trailingPE"]}")
print(f"52 Week High: ${info["fiftyTwoWeekHigh"]}")
print(f"52 Week Low: ${info["fiftyTwoWeekLow"]}")
print(f"Open: ${info["open"]}")
print(f"Previous Close: ${info["previousClose"]}")