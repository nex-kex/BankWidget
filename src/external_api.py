import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(amount: float, currency: str) -> float:
    """Конвертирует сумму транзакции в USD или EUR в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    result = requests.get(url, {"apikey": API_KEY})
    return result.json()["result"]
