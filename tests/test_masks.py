import pytest
from unittest.mock import patch

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected_mask",
    [("7000792289606361", "7000 79** **** 6361"), (7000792289606361, "7000 79** **** 6361"),
     ("700079228960636", "7000 79** **** 0636"), (700079228960636, "7000 79** **** 0636")],
)
def test_get_mask_card_number(card_number, expected_mask):
    assert get_mask_card_number(card_number) == expected_mask


@patch("builtins.str")
def test_get_mask_card_number_exception(mock_str):
    mock_str.return_value = {}
    with pytest.raises(TypeError):
        get_mask_card_number("")


@pytest.mark.parametrize(
    "account, expected_mask", [("73654108430135874305", "**4305"), (73654108430135874305, "**4305"),
                               ("3654108430135874305", "**4305"), (3654108430135874305, "**4305")]
)
def test_get_mask_account(account, expected_mask):
    assert get_mask_account(account) == expected_mask


@patch("builtins.str")
def test_get_mask_account_exception(mock_str):
    mock_str.return_value = {}
    with pytest.raises(TypeError):
        get_mask_account("")
