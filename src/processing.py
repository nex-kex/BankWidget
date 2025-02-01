def filter_by_state(list_of_transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и возвращает новый с теми элементами,
    у которых ключ state соответствует указанному значению (по умолчанию - "EXECUTED")
    """
    new_transaction_list = []
    for transaction in list_of_transactions:
        if transaction.get("state") == state:
            new_transaction_list.append(transaction)
    return new_transaction_list


def sort_by_date(list_of_transactions: list[dict], descending: bool = True) -> list[dict]:
    """
    Функция принимает список словарей и порядок сортировки (тип bool, по умолчанию - убывание(True)),
    возвращает отсортированный по дате список операций
    """
    list_of_transactions = [t for t in list_of_transactions if t.get("date")]
    new_transaction_list = sorted(list_of_transactions, key=lambda x: x["date"], reverse=descending)
    return new_transaction_list
