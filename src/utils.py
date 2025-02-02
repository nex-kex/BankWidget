import json
import logging
import os

from src.external_api import convert_to_rub

log_path = "../logs/utils.log"

# Устраняет ошибку отсутствия файла при импорте модуля
if str(os.path.dirname(os.path.abspath(__name__)))[-3:] != "src":
    log_path = log_path[1:]


logger = logging.getLogger("utils")
file_handler = logging.FileHandler(log_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_info(file_path: str) -> list[dict]:
    """Возвращает список словарей с данными о финансовых транзакциях из JSON-файла"""

    try:
        with open(file_path, encoding="utf-8") as f:
            logger.info(f"Loading transactions from {file_path}...")
            transactions = json.load(f)

        for transaction in transactions:
            if transaction.get("operationAmount"):
                amount = transaction["operationAmount"]["amount"]
                name = transaction["operationAmount"]["currency"]["name"]
                code = transaction["operationAmount"]["currency"]["code"]

                del transaction["operationAmount"]

                transaction["amount"] = round(float(amount), 2)
                transaction["currency_name"] = name
                transaction["currency_code"] = code

    except Exception as ex:
        logger.error(f"Exception occurred: {ex}")
        return []

    return transactions


def get_transaction_amount(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях"""

    try:
        if transaction.get("amount"):
            currency = transaction["currency_code"]

            if currency == "RUB":
                logger.info("Transaction's amount in RUB.")
                return transaction["amount"]

            else:
                logger.info("Converting transaction's amount to RUB...")
                return convert_to_rub(transaction["amount"], currency)

        else:
            logger.warning("Could not determine transaction's amount.")
            return 0

    except Exception as ex:
        logger.error(f"Exception occurred: {ex}")
        return 0
