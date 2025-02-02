from unittest.mock import patch

from src.main import (get_currency_sorted_transactions, get_date_sorted_transactions, get_state_sorted_transactions,
                      get_transactions, print_result)


@patch("src.utils.get_transactions_info")
def test_get_transactions_json(mock_get_transactions_info):
    mock_get_transactions_info.return_value = []
    assert get_transactions("1") == []


@patch("src.read_from_table.read_from_csv")
def test_get_transactions_csv(mock_read_from_csv):
    mock_read_from_csv.return_value = []
    assert get_transactions("1") == []


@patch("src.read_from_table.read_from_xlsx")
def test_get_transactions_xlsx(mock_read_from_xlsx):
    mock_read_from_xlsx.return_value = []
    assert get_transactions("1") == []


def test_get_state_sorted_transactions(RUS_transaction):
    assert get_state_sorted_transactions([RUS_transaction], "EXECUTED") == []


def test_get_date_sorted_transactions_descending(list_of_transactions):
    assert get_date_sorted_transactions(list_of_transactions, "да", "по убыванию") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_get_date_sorted_transactions_ascending(list_of_transactions):
    assert get_date_sorted_transactions(list_of_transactions, "да", "по возрастанию") == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_get_date_sorted_transactions_no_sort(list_of_transactions):
    assert get_date_sorted_transactions(list_of_transactions, "нет") == list_of_transactions


def test_get_currency_sorted_transactions(RUS_transaction, transactions):
    assert get_currency_sorted_transactions([RUS_transaction], "да") == [RUS_transaction]
    assert get_currency_sorted_transactions(transactions, "нет") == transactions


@patch("src.widget.get_date")
def test_print_result(mock_date):
    mock_date.return_value = "date"
    assert print_result([]) is None
    assert (
        print_result(
            [
                {
                    "description": "description",
                    "date": "date",
                    "to": "to",
                    "amount": "amount",
                    "currency_name": "currency_name",
                }
            ]
        )
        is None
    )
    assert (
        print_result(
            [
                {
                    "description": "description",
                    "date": "date",
                    "to": "to",
                    "from": "from",
                    "amount": "amount",
                    "currency_name": "currency_name",
                }
            ]
        )
        is None
    )
