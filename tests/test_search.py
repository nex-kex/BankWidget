from src.search import search_transactions, filter_by_category
from tests.conftest import csv_transactions


def test_search_transactions(csv_transactions):
    assert search_transactions(csv_transactions, "9") == csv_transactions


def test_search_transactions_empty():
    assert search_transactions([], "line") == []


def test_filter_by_category(csv_transactions):
    assert filter_by_category(csv_transactions) == {"9": 1, "99": 1}


def test_filter_by_category_with_category(csv_transactions):
    assert filter_by_category(csv_transactions, ["9"]) == {"9": 1}
