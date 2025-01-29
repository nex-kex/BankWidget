import json
import logging

from src.external_api import convert_to_rub

log_path = "../logs/utils.log"

# Устраняет ошибку отсутствия файла при импорте модуля
if __name__ != "__main__":
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

    except Exception as ex:
        logger.error(f"Exception occurred: {ex}")
        return []

    return transactions


def get_transaction_amount(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях"""

    try:
        if transaction.get("operationAmount"):
            currency = transaction["operationAmount"]["currency"]["code"]

            if currency == "RUB":
                logger.info("Transaction's amount in RUB.")
                return transaction["operationAmount"]["amount"]

            else:
                logger.info("Converting transaction's amount to RUB...")
                return convert_to_rub(transaction["operationAmount"]["amount"], currency)

        else:
            logger.warning("Could not determine transaction's amount.")
            return 0

    except Exception as ex:
        logger.error(f"Exception occurred: {ex}")
        return 0
