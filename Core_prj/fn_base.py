class pas_tres_class:

    def get_coin_data(self, ID):
        """
        From the URL, add a listing number of the coin to get all the data in
        a JSON format
        """
        r = requests.get('https://api.coinmarketcap.com/v2/ticker/' + str(ID))
        return r.json()


    def get_listing(self):
        """
        The URL gives the listing of every coin referenced in coinmarketcap
        It will be used to get data of every coin
        """
        # Get the last updated listing list
        r = requests.get('https://api.coinmarketcap.com/v2/listings/')
        self.output_listing(r.json())
        return r.json()


    def output_listing(self, data):
        """
        Write the list of listing in a csv file
        """
        cpt = 0
        with open("Output/listing.csv", "a+") as att_file:
            total_id = len(data["data"]) - 1
            while cpt <= total_id:
                symbol = data["data"][cpt]["symbol"]
                name = data["data"][cpt]["name"]
                id = data["data"][cpt]["id"]
                att_file.write(symbol + "," + name + "," + str(id) + "\n")
                cpt += 1
        return 0
