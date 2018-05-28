import json
import requests


def get_listing():
    # Get the last updated listing list
	r = requests.get('https://api.coinmarketcap.com/v2/listings/')
	return r.json()

	# """ For test we will use a json file locally, the above code works and will
	# download the last updated data """
    #
	# json_data=open("listing_test.json").read()
	# data = json.loads(json_data)
	# return data

def output(result):
    # Write the list in a csv file - easier to use (at least to me)
    cpt = 0
    with open("listing.csv", "a+") as att_file:
        total_id = len(result["data"]) - 1
        while cpt <= total_id:
            symbol = result["data"][cpt]["symbol"]
            name = result["data"][cpt]["name"]
            id = result["data"][cpt]["id"]
            att_file.write(name + "," + symbol + "," + str(id) + "\n")
            cpt += 1

def main():
	result = get_listing()
	if result:
		output(result)


if __name__ == '__main__':
	main()
