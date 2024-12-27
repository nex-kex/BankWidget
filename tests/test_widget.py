import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("account_card, expected_mask", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353")
])
def test_mask_account_card(account_card, expected_mask):
    assert mask_account_card(account_card) == expected_mask


@pytest.mark.parametrize("date, expected_date", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2005-04-21T11:04:75.467404", "21.04.2005")
])
def test_get_date(date, expected_date):
    assert get_date(date) == expected_date
