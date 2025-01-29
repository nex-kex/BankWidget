import csv

import pandas as pd


def read_from_csv(file_name: str) -> list[dict]:
    """Читает CSV-файл file_name с транзакциями и возвращает из в виде списка словарей."""
    with open(file_name, "r", encoding="utf-8") as csv_file:
        transactions = list(csv.DictReader(csv_file, delimiter=";"))
        return transactions


def read_from_xlsx(xlsx_file: str) -> list[dict]:
    """Читает XLSX-файл file_name с транзакциями и возвращает из в виде списка словарей."""
    data = pd.read_excel(xlsx_file)
    transactions = data.to_dict(orient='records')
    return transactions
