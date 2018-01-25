import re
import numpy as np


class Order:
	def __init__(self, symbol, amount, buy_price, expected_price, current_price=0):
		self.symbol = symbol
		self.amount = amount
		self.buy_price = buy_price
		self.expected_price = expected_price
		self.reference_currency = "BTC" # assume BTC
		self.trade_currency = re.split("BTC$", symbol)[0]
		self.current_price = current_price