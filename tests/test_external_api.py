import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import convert_to_rub

load_dotenv()
API_KEY = os.getenv("API_KEY")


@patch("requests.get")
def test_external_api(mock_get):
    mock_get.return_value.json.return_value = {"result": 123.45}
    assert convert_to_rub(1, "USD") == 123.45

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"
    mock_get.assert_called_once_with(url, {"apikey": API_KEY})
