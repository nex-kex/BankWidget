import re
from collections import Counter


def search_transactions(transactions_list: list[dict], search_info: str) -> list[dict]:
    """Функция принимает список словарей с данными о транзакциях и возвращает список тех транзакций,
    в описании которых есть строка поиска (search_info)."""

    filtered_transactions = []

    for transaction in transactions_list:
        if transaction.get("description"):
            if re.findall(search_info.lower(), transaction["description"].lower()):
                filtered_transactions.append(transaction)

    return filtered_transactions


def filter_by_category(transactions_list: list[dict], categories_list: list[str] = []) -> dict:
    """Функция принимает список словарей с данными о транзакциях и список категорий операций,
    а возвращает словарь, где ключи - названия категорий, а значения - количество операций в данной категории."""

    all_categories = [
        transaction["description"] for transaction in transactions_list if transaction.get("description")
    ]
    counted_categories = Counter(all_categories)

    searched_categories = {}

    if len(categories_list):
        for category in categories_list:
            searched_categories[category] = counted_categories[category]

    else:
        searched_categories = counted_categories

    return searched_categories
