from binance.client import Client
import re


def get_all_symbols(bi_client):
	all_symbols = bi_client.get_all_tickers()
	return [s["symbol"] for s in all_symbols]


def get_all_btc_symbols(bi_client):
	return [s for s in get_all_symbols(bi_client) if len(re.findall("BTC$", s))]


def get_all_eth_symbols(bi_client):
	return [s for s in get_all_symbols(bi_client) if len(re.findall("ETH$", s))]


def get_all_bnb_symbols(bi_client):
	return [s for s in get_all_symbols(bi_client) if len(re.findall("BNB$", s))]


def get_all_usdt_symbols(bi_client):
	return [s for s in get_all_symbols(bi_client) if len(re.findall("USDT$", s))]


def get_current_price(bi_client, symbol_pair):
	return float(bi_client.get_symbol_ticker(symbol=symbol_pair)["price"])


def get_current_value(client, orders):
	return sum([get_current_price(client, order.symbol)*order.amount for order in orders])


def write_orders_to_file(file_name, orders):
	with open(file_name, "a") as file:
		for order in orders:
			file.write(str(order.symbol) + "," + 
					   str(order.amount) + "," +
					   str(order.buy_price) + "," +
					   str(order.expected_price) + "," +
					   str(order.current_price) + "," +
					   str(order.current_price*order.amount))
			file.write("\n")

		file.write("\n----------------------------------\n")