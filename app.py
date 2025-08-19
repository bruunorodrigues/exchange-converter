import requests
from validation import valid_value
import os
API_URL = "https://api.exchangerate-api.com/v4/latest/"

def check_rate(exchange):
    response = requests.get(API_URL + exchange.upper())
    if response.status_code == 200:
        return response.json()['rates']
    return f'Error: {response.status_code}'

def convert(exchange, destination_exchange, value):  
    rate = check_rate(exchange.upper())
    if isinstance(rate, dict):
        os.system('cls')
        if destination_exchange.upper() in rate:
            os.system('cls')
            data = rate[destination_exchange.upper()]
            converted = value * data
            return converted
        else:
            return f'Exchange rate for {destination_exchange} not found.'
    return f'Exchange rate for {exchange} not found.'

while True:
    insert_exchange = input('Which is your exchange rate (ex: USD, BRL, EUR, etc)? ').strip().upper()
    os.system('cls')
    insert_exchange_destination = input('Which exchange rate do you want to convert to (ex: USD, BRL, EUR, etc)? ').strip().upper()
    os.system('cls')

    if check_rate(insert_exchange) is not None:
        os.system('cls')
        break
    else:
        print(f"Invalid currency {insert_exchange}. Please try again with a valid one.")

value_converter = valid_value()

result = convert(insert_exchange, insert_exchange_destination, value_converter)

if isinstance(result, float):
    os.system('cls')
    print("=== Conversor de Moedas ===")
    print(f'{value_converter} {insert_exchange} = {result:.2f} {insert_exchange_destination}')
else:
    print(result)