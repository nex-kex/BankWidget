from unittest.mock import patch, mock_open

from src.utils import get_transaction_amount, get_transactions_info


def test_get_transactions_info_exception():
    assert get_transactions_info("file") == []


@patch("builtins.open", mock_open(read_data=""))
def test_get_transactions_info():
    assert get_transactions_info("./data/operations.json") == []


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
        get_transaction_amount({"operationAmount": {"amount": 1, "currency": {"name": "USD", "code": "USD"}}})
        == 123.45
    )


def test_get_transaction_amount_no_amount():
    assert get_transaction_amount({}) == 0


def test_get_transaction_amount_exception():
    assert get_transaction_amount("") == 0
