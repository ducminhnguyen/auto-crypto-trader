import os
import sys
import json
from binance.client import Client
import helper
import choosepair
import order
import time
import numpy as np

CONFIG_FILE = "config.json"
BALANCE = 0.0


if __name__ == "__main__":
	
	api_params = json.load(open(CONFIG_FILE))
	BALANCE = api_params["DEMO_AMOUNT"]

	client = Client(api_params["API_KEY"], api_params["API_SECRET"])
	btc_syms = helper.get_all_btc_symbols(client)
	
	chosen_pair = choosepair.choose_random_pair(btc_syms, api_params["K"])
	print(chosen_pair)

	open_orders = []
	change_time = np.zeros((1, api_params["K"]))

	for sym in chosen_pair:
		current_price = helper.get_current_price(client, sym)
		allocated_value = BALANCE / api_params["K"]
		open_orders.append(order.Order(sym, allocated_value / current_price, 
			current_price, current_price*api_params["E"], current_price))

	total_value = 0
	while True:
		for order in open_orders:
			current_price = helper.get_current_price(client, order.symbol)
			order.current_price = current_price
			if current_price >= order.expected_price:
				idx = open_orders.index(order)
				old_symbol = order.symbol
				current_order_btc = order.expected_price*order.amount
				new_pair = choosepair.choose_random_pair(btc_syms, 1)[0]
				new_pair_current_price = helper.get_current_price(client, new_pair)
				order = order.Order(new_pair, current_order_btc / new_pair_current_price, 
					new_pair_current_price, new_pair_current_price*api_params["E"], new_pair_current_price)
				print("Change pair at %d, symbol %s -> %s" % (idx, old_symbol, new_pair))
				change_time[idx] += 1

		print("Current value: %f" % (helper.get_current_value(client, open_orders)))
		print(change_time)
		time.sleep(60)



