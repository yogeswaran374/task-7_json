import requests
#define countrydata class
class countrydata:
#constructor for taking input
    def __init__(self): 
        self.url="https://restcountries.com/v3.1/all"
        self.data=self.fetch_data()
# create method to fetch data from the url
    def fetch_data(self):
        response=requests.get(self.url)
        if response.status_code==200:
            return response.json()
        else:
            print("error")
            return None
# create method it shows name of country ,currencies and symbol
    def country_info(self):
            if self.data:
                for country in self.data:
                    name = country['name']['common']
                    currencies = country.get('currencies', {})  # Use get method to handle missing 'currencies' key
                    print(name)
                    print("currencies:")
                    for currency, details in currencies.items():
                        symbol = details.get('symbol')
                        print(f"{currency}:{symbol}")
                    print()
    def country_dollar(self):
            if self.data:
                for country in self.data:
                    name = country['name']['common']
                    currencies = country.get('currencies', {})  # Use get method to handle missing 'currencies' key
                    for currencies, details in currencies.items():
                        symbol = details.get('symbol')
                        if symbol =="$":
                             print(name)
    def country_Euro(self):
            if self.data:
                for country in self.data:
                    name = country['name']['common']
                    currencies = country.get('currencies', {})  # Use get method to handle missing 'currencies' key
                    for currencies, details in currencies.items():
                        symbol = details.get('symbol')
                        if symbol =="€":
                             print(name)
country_data=countrydata()
country_data.country_info()
country_data.country_dollar()
country_data.country_Euro()