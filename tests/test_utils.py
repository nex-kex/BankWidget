from unittest.mock import patch

from src.utils import get_transaction_amount, get_transactions_info


def test_get_transactions_info_no_file():
    assert get_transactions_info("file") == []


@patch("json.load")
def test_get_transactions_info_empty(mock_load):
    mock_load.return_value = {}
    assert get_transactions_info("../data/operations.json") == []


def test_get_transaction_amount_empty():
    assert get_transaction_amount({}) == 0


def test_get_transaction_amount_rus(RUS_transaction):
    assert get_transaction_amount(RUS_transaction) == 42210.20
