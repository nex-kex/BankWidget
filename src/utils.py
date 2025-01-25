import json

from src.external_api import convert_to_rub


def get_transactions_info(file_path: str) -> list[dict]:
    """Возвращает список словарей с данными о финансовых транзакциях из JSON-файла"""

    try:
        with open(file_path, encoding="utf-8") as f:
            transactions = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

    return transactions


def get_transaction_amount(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях"""
    if transaction.get("operationAmount"):
        currency = transaction["operationAmount"]["currency"]["code"]
        if currency == "RUB":
            return transaction["operationAmount"]["amount"]
        else:
            return convert_to_rub(transaction["operationAmount"]["amount"], currency)
    else:
        return 0
