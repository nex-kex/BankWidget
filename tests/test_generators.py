import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected_list",
    [
        (
            "RUB",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "amount": "43318.34",
                    "currency_name": "руб.",
                    "currency_code": "RUB",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "amount": "67314.70",
                    "currency_name": "руб.",
                    "currency_code": "RUB",
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
        ),
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "amount": "9824.07",
                    "currency_name": "USD",
                    "currency_code": "USD",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "amount": "79114.93",
                    "currency_name": "USD",
                    "currency_code": "USD",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "amount": "56883.54",
                    "currency_name": "USD",
                    "currency_code": "USD",
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
        ),
    ],
)
def test_filter_by_currency(transactions, currency, expected_list):
    assert list((filter_by_currency(transactions, currency))) == expected_list


def test_filter_by_currency_no_result():
    assert (
        list(
            filter_by_currency(
                [
                    {
                        "id": 939719570,
                        "state": "EXECUTED",
                        "date": "2018-06-30T02:08:58.425572",
                        "amount": "9824.07",
                        "currency_name": "USD",
                        "currency_code": "USD",
                        "description": "Перевод организации",
                        "from": "Счет 75106830613657916952",
                        "to": "Счет 11776614605963066702",
                    }
                ],
                "RUB",
            )
        )
        == []
    )


def test_filter_by_currency_empty_list():
    assert list(filter_by_currency([], "RUB")) == []


def test_transaction_descriptions(transactions):
    assert list(transaction_descriptions(transactions)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_transaction_descriptions_empty_list():
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start, stop, expected_list",
    [
        (
            6,
            11,
            [
                "0000 0000 0000 0006",
                "0000 0000 0000 0007",
                "0000 0000 0000 0008",
                "0000 0000 0000 0009",
                "0000 0000 0000 0010",
                "0000 0000 0000 0011",
            ],
        ),
        (1, 1, ["0000 0000 0000 0001"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start, stop, expected_list):
    assert list(card_number_generator(start, stop)) == expected_list
