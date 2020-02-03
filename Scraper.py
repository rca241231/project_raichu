import csv

class Scrape:
    def __init__(self):
        self.CHROME_DRIVER_PATH = './chromedriver'

    def write_output(self, data):
        with open('data.csv', mode='w') as output_file:
            writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

            # Header
            writer.writerow([
                "mls",
                "mls_status",
                "price",
                "hoa",
                "sqft",
                "price_per_sqft",
                "lot_size",
                "beds",
                "baths",
                "stories",
                "street",
                "city",
                "state",
                "zip_code",
                "sold_date",
                "year_built",
                "time_on_redfin",
                "url"
            ])

            # Body
            for row in data:
                writer.writerow(row)

    def fetch_data(self):
        pass

    def scrape(self):
        self.fetch_data()
        self.write_output(self.data)
