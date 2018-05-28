import json
import requests


def get_coin_data():
	# r = requests.get('https://api.coinmarketcap.com/v2/ticker/1/' + choice)
	# #for coin in r.json():
	# #    print(coin["price_usd"])
	# return r.json()

	""" For test we will use a json file locally, the above code works and will
	download the last updated data """

	json_data=open("test.json").read()
	data = json.loads(json_data)
	return data

def output(result):
	#with open("output.csv", "a+") as att_file:
	print result



def main():
	result = get_coin_data()
	if result:
		output(result)


if __name__ == '__main__':
	main()
