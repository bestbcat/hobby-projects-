import requests
import variables
Currency_URL=f"https://v6.exchangerate-api.com/v6/{variables.api_key}/latest/"

def APICALL(Currency):
    URL = f"{Currency_URL}{Currency}"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data from API, status code: {response.status_code}")

currency_name = input(f"what currency do you want to convert? \n write the currency code (e.g. USD, EUR, GBP): ")
inforeturn = input(f"what currency do you want to convert to? \n write the currency code (e.g. USD, EUR, GBP): ")

multiplier = input(f"how much {currency_name} do you want to convert? (e.g. 100): ")

info = APICALL(currency_name)

if info:

    num1 = float(multiplier) * info['conversion_rates'][inforeturn]

    conversion_rate = info['conversion_rates'][inforeturn]
    print(f"{multiplier} {currency_name} is equal to {num1} {inforeturn}")