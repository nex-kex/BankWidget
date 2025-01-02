from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction

    # ошибка - окончание списка


def transaction_descriptions(transactions: list[dict], currency: str) -> Iterator[str]:
    """Генератор, который возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]

    # ошибка - окончание списка


def card_number_generator(start: int, finish: int) -> Iterator[str]:
    """Генератор, который выдает номера банковских карт в определённом формате"""
    int_card_number = start

    while int_card_number <= finish:
        str_card_number = str(int_card_number)
        while len(str_card_number) != 16:
            str_card_number = "0" + str_card_number
        card_number = f"{str_card_number[:5]} {str_card_number[4:9]} {str_card_number[8:13]} {str_card_number[12:]}"
        yield card_number
        int_card_number += 1
