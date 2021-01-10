import requests

def get_price(which):
	r = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={which}EUR').json()['result'][f'X{which}ZEUR']['a'][0]
	r2 = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={which}USD').json()['result'][f'X{which}ZUSD']['a'][0]

	return r, r2
