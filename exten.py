import requests
import json
from tkn import currency


class ConvException(Exception):
    pass


class GetCurrency:

    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        base = base.lower()
        quote = quote.lower()

        if base == quote:
            raise ConvException('Попытка перевода одинаковых валют.')

        try:
            base_curr = currency[base]
        except KeyError:
            raise ConvException(f'Некорректно обработана валюта "{base}"')

        try:
            quote_curr = currency[quote]
        except KeyError:
            raise ConvException(f'Некорректно обработана валюта "{quote}"')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvException(f'Некорректно обработан параметр количества валюты "{amount}"')

        r1 = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_curr}&tsyms={quote_curr}')
        res = json.loads(r1.content)[quote_curr] * amount

        return res
