from unittest.mock import mock_open, patch

from src.utils import get_transaction_amount, get_transactions_info


def test_get_transactions_info_exception():
    assert get_transactions_info("file") == []


@patch("builtins.open", mock_open(read_data="""[{
    "id": 200634844,
    "state": "CANCELED",
    "date": "2018-02-13T04:43:11.374324",
    "operationAmount": {
      "amount": "42210.20",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 33355011456314142963",
    "to": "Счет 45735917297559088682"
  }]"""))
def test_get_transactions_info(RUS_transaction):
    assert get_transactions_info("./data/operations.json") == [RUS_transaction]


@patch("json.load")
def test_get_transactions_info_empty(mock_load, csv_transactions):
    mock_load.return_value = csv_transactions
    assert get_transactions_info("./data/operations.json") == csv_transactions


def test_get_transaction_amount_empty():
    assert get_transaction_amount({}) == 0


def test_get_transaction_amount_rus(RUS_transaction):
    assert get_transaction_amount(RUS_transaction) == 42210.20


@patch("requests.get")
def test_get_transaction_amount_not_rus(mock_get):
    mock_get.return_value.json.return_value = {"result": 123.45}
    assert (
        get_transaction_amount({"amount": 1, "currency_name": "USD", "currency_code": "USD"})
        == 123.45
    )


def test_get_transaction_amount_no_amount():
    assert get_transaction_amount({}) == 0


def test_get_transaction_amount_exception():
    assert get_transaction_amount("") == 0
