import requests
import json
import time
from Scraper import Scrape

DAYS = 1095

class Scraper(Scrape):
    def __init__(self):
        Scrape.__init__(self)
        self.seen = []
        self.data = []

    def fetch_data(self):
        mls_list = []
        mls_status_list = []
        price_list = []
        hoa_list = []
        sqft_list = []
        price_per_sqft_list = []
        lot_size_list = []
        beds_list = []
        baths_list = []
        stories_list = []
        street_list = []
        city_list = []
        state_list = []
        zip_code_list = []
        sold_date_list = []
        year_built_list = []
        time_on_redfin_list = []
        url_list = []

        cookies = {
            'RF_BROWSER_ID': '2NxZEe6kQM2Q2WgAKFz_eg',
            'RF_BID_UPDATED': '1',
            '_gcl_au': '1.1.1270246981.1579716827',
            '_ga': 'GA1.2.851788768.1579716828',
            '_fbp': 'fb.1.1579716827563.652346914',
            'G_ENABLED_IDPS': 'google',
            '__gads': 'ID=5374cf7bba77521e:T=1579716831:S=ALNI_MaH7ba8HN3nX0IvNClHx9HtiWUwqw',
            'RF_LAST_USER_ACTION': '1579716850684%3Ab42a636690305f355370df894244331af6c933c2',
            'RF_PARTY_ID': '4293663',
            'RF_AUTH': 'f8bf844320ec910ff506452a14b938af130a2b52',
            'RF_W_AUTH': 'f8bf844320ec910ff506452a14b938af130a2b52',
            'RF_SECURE_AUTH': 'baf068aafd5bd27ea5bfdb76787d50f93041a4f5',
            'RF_ACCESS_LEVEL': '3',
            'JSESSIONID': 'C2C01180A762118E1C12A96F5978FABA',
            'save_search_nudge_flyout': '1%251579716856852%25false',
            'RF_LAST_ACCESS': '1579717693886%3Aba29a606974c92a7d217158ad0ace8175581faba',
            '__utmx': '222895640.shO3i6adRPWNFY-OQyD5Lw$0:2.Syki4KXHTMGcd4wXS3oo3w$0:0.EL-l5V5_TraMAoyBl8zA2Q$0:0.HPaeM5zMSp-5hxCpNhjEDg$0:0',
            'iterableEndUserId': 'richard.chen.1989%40gmail.com',
            '__utmxx': '222895640.shO3i6adRPWNFY-OQyD5Lw$0:1580322626:8035200.Syki4KXHTMGcd4wXS3oo3w$0:1580059726:8035200:.EL-l5V5_TraMAoyBl8zA2Q$0:1580247718:8035200:.HPaeM5zMSp-5hxCpNhjEDg$0:1580149442:8035200:',
            'RF_CORVAIR_LAST_VERSION': '299.3.0',
            '_gid': 'GA1.2.498157996.1580681045',
            'RF_MARKET': 'sanfrancisco',
            'RF_LISTING_VIEWS': '115094742.114386858.27753221.111726473.115768204.115770935.115746038.114903048.115719858.110832682.112860708.112335858.112908224.110805768.104624660.114762905.115269746.84798458.115657197.115442477',
            'RF_BROWSER_CAPABILITIES': '%7B%22css-transitions%22%3Atrue%2C%22css-columns%22%3Atrue%2C%22css-generated-content%22%3Atrue%2C%22css-opacity%22%3Atrue%2C%22events-touch%22%3Afalse%2C%22geolocation%22%3Atrue%2C%22screen-size%22%3A4%2C%22screen-size-tiny%22%3Afalse%2C%22screen-size-small%22%3Afalse%2C%22screen-size-medium%22%3Afalse%2C%22screen-size-large%22%3Afalse%2C%22screen-size-huge%22%3Atrue%2C%22html-prefetch%22%3Afalse%2C%22html-range%22%3Atrue%2C%22html-form-validation%22%3Atrue%2C%22html-form-validation-with-required-notice%22%3Atrue%2C%22html-input-placeholder%22%3Atrue%2C%22html-input-placeholder-on-focus%22%3Atrue%2C%22ios-app-store%22%3Afalse%2C%22google-play-store%22%3Afalse%2C%22ios-web-view%22%3Afalse%2C%22android-web-view%22%3Afalse%2C%22activex-object%22%3Atrue%2C%22webgl%22%3Atrue%2C%22history%22%3Atrue%2C%22localstorage%22%3Atrue%2C%22sessionstorage%22%3Atrue%2C%22position-fixed-workaround%22%3Afalse%2C%22passive-event-listener%22%3Atrue%7D',
            'AKA_A2': 'A',
            'AMP_TOKEN': '%24NOT_FOUND',
            'unifiedLastSearch': 'name%3DSan%2520Jose%26subName%3DSan%2520Jose%252C%2520CA%252C%2520USA%26url%3D%252Fcity%252F17420%252FCA%252FSan-Jose%26id%3D9_17420%26type%3D2%26isSavedSearch%3D%26countryCode%3DUS',
            'nhfy_badgecount': '20',
            'RF_BUSINESS_MARKET': '2',
            '_dc_gtm_UA-294985-1': '1',
            '_gat_UA-294985-1': '1',
            'RF_LAST_SEARCHED_CITY': 'Fremont',
            'ki_t': '1579716833252%3B1580682871189%3B1580698515122%3B5%3B34',
            'RF_VISITED': 'null',
            'userPreferences': 'parcels%3Dtrue%26schools%3Dfalse%26mapStyle%3Ds%26statistics%3Dtrue%26agcTooltip%3Dfalse%26agentReset%3Dfalse%26ldpRegister%3Dfalse%26afCard%3D2%26schoolType%3D0%26lastSeenLdp%3DnoSharedSearchCookie%26viewedSwipeableHomeCardsDate%3D1580698515728',
        }

        headers = {
            'authority': 'www.redfin.com',
            'x-newrelic-id': 'VQMDUFFaGwQJU1hSBAc=',
            'dnt': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'referer': 'https://www.redfin.com/city/17420/CA/San-Jose/filter/property-type=house,min-price=400k,hoa=0,include=sold-3mo,viewport=37.60931:37.34448:-121.38193:-122.72775,no-outline',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
        }
        params = (
            ('al', '3'),
            ('hoa', '0'),
            ('market', 'sanfrancisco'),
            ('min_stories', '1'),
            ('num_homes', '10000'),
            ('ord', 'redfin-recommended-asc'),
            ('page_number', '2'),
            ('poly', '-122.62338 37.28987,-121.27756 37.28987,-121.27756 37.55489,-122.62338 37.55489,-122.62338 37.28987'),
            ('sold_within_days', str(DAYS)),
            ('start', '0'),
            ('status', '9'),
            ('uipt', '1'),
            ('v', '8'),
            ('zoomLevel', '10'),
        )
        homes = json.loads(requests.get('https://www.redfin.com/stingray/api/gis', headers=headers, params=params, cookies=cookies).text.replace('{}&&', ''))['payload']['homes']
        size = len(homes)
        print(f"Received {size} houses for {DAYS} days.")

        for home in homes:
            mls = home['mlsId']['value'] if 'mlsId' in home.keys() and 'value' in home['mlsId'].keys() else 'Unknown'

            if mls not in self.seen:
                mls_status = home['mlsStatus'] if 'mlsStatus' in home.keys() else 'Unknown'

                price = home['price']['value'] if 'price' in home.keys() and 'value' in home['price'].keys() else 'Unknown'

                hoa = home['hoa']['value'] if 'hoa' in home.keys() and 'value' in home['hoa'].keys() else '0'

                sqft = home['sqFt']['value'] if 'sqFt' in home.keys() and 'value' in home['sqFt'].keys() else 'Unknown'

                price_per_sqft = home['pricePerSqFt']['value'] if 'pricePerSqFt' in home.keys() and 'value' in home['pricePerSqFt'].keys() else 'Unknown'

                lot_size = home['lotSize']['value'] if 'lotSize' in home.keys() and 'value' in home['lotSize'].keys() else 'Unknown'

                beds = home['beds'] if 'beds' in home.keys() else 'Unknown'

                baths = home['baths'] if 'baths' in home.keys() else 'Unknown'

                stories = home['stories'] if 'stories' in home.keys() else '1'

                street = home['streetLine']['value'] if 'streetLine' in home.keys() and 'value' in home['streetLine'].keys() else 'Unknown'

                city = home['city'] if 'city' in home.keys() else 'Unknown'

                state = home['state'] if 'state' in home.keys() else 'Unknown'

                zip_code = home['zip'] if 'zip' in home.keys() else 'Unknown'

                sold_date = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(float(home['soldDate'])/1000)) if 'soldDate' in home.keys() else 'Unknown'

                year_built = home['yearBuilt']['value'] if 'yearBuilt' in home.keys() and 'value' in home['yearBuilt'].keys() else 'Unknown'

                time_on_redfin = home['timeOnRedfin']['value']/(1000 * 60 * 60 * 24) if 'timeOnRedfin' in home.keys() and 'value' in home['timeOnRedfin'].keys() else 'Unknown'

                url = 'https://www.redfin.com/' + home['url']

                # Store data
                mls_list.append(mls)
                mls_status_list.append(mls_status)
                price_list.append(price)
                hoa_list.append(hoa)
                sqft_list.append(sqft)
                price_per_sqft_list.append(price_per_sqft)
                lot_size_list.append(lot_size)
                beds_list.append(beds)
                baths_list.append(baths)
                stories_list.append(stories)
                street_list.append(street)
                city_list.append(city)
                state_list.append(state)
                zip_code_list.append(zip_code)
                sold_date_list.append(sold_date)
                year_built_list.append(year_built)
                time_on_redfin_list.append(time_on_redfin)
                url_list.append(url)
                self.seen.append(mls)

        for (
            mls,
            mls_status,
            price,
            hoa,
            sqft,
            price_per_sqft,
            lot_size,
            beds,
            baths,
            stories,
            street,
            city,
            state,
            zip_code,
            sold_date,
            year_built,
            time_on_redfin,
            url
        ) in zip(
            mls_list,
            mls_status_list,
            price_list,
            hoa_list,
            sqft_list,
            price_per_sqft_list,
            lot_size_list,
            beds_list,
            baths_list,
            stories_list,
            street_list,
            city_list,
            state_list,
            zip_code_list,
            sold_date_list,
            year_built_list,
            time_on_redfin_list,
            url_list
        ):
            self.data.append(
                [
                    mls,
                    mls_status,
                    price,
                    hoa,
                    sqft,
                    price_per_sqft,
                    lot_size,
                    beds,
                    baths,
                    stories,
                    street,
                    city,
                    state,
                    zip_code,
                    sold_date,
                    year_built,
                    round(float(time_on_redfin), 2) if time_on_redfin != 'Unknown' else time_on_redfin,
                    url
                ]
            )


scrape = Scraper()
scrape.scrape()
