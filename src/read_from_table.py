import csv

import pandas as pd


def read_from_csv(file_name: str) -> list[dict]:
    """Читает CSV-файл file_name с транзакциями и возвращает из в виде списка словарей."""
    with open(file_name, "r", encoding="utf-8") as csv_file:
        transactions = []
        data = csv.DictReader(csv_file, delimiter=";")
        for i in data:
            transactions.append(i)
        return transactions


def read_from_xlsx(xlsx_file: str) -> list[dict]:
    """Читает XLSX-файл file_name с транзакциями и возвращает из в виде списка словарей."""
    transactions = []
    data = pd.read_excel(xlsx_file)

    # Список ключей для каждой транзакции
    keys = []
    for i in data:
        keys.append(i)

    for _, row in data.iterrows():
        row_dict = {}
        i = 0
        for info in row:
            row_dict[keys[i]] = info
            i += 1
        transactions.append(row_dict)

    return transactions