from read_from_table import read_from_csv, read_from_xlsx
from utils import get_transactions_info
from processing import filter_by_state, sort_by_date
from generators import filter_by_currency
from search import search_transactions
from widget import get_date, mask_account_card


if __name__ == "__main__":

    # Тип данных, с которыми будет работать программа
    fyle_type = input("""Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
""")

    while fyle_type not in ["1", "2", "3"]:
        fyle_type = input("Пожалуйста, введите число от 1 до 3.\n")

    transactions = []
    if fyle_type == "1":
        transactions = get_transactions_info("../data/operations.json")
        print("Для обработки выбран JSON-файл.\n")
    elif fyle_type == "2":
        transactions = read_from_csv("../data/transactions.csv")
        print("Для обработки выбран CSV-файл.\n")
    elif fyle_type == "3":
        transactions = read_from_xlsx("../data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.\n")


    # Статус для сортировки
    status_type = input("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""").upper()
    while status_type not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Статус операции "{status_type}" недоступен.\n')
        status_type = input("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""").upper()

    transactions_by_status = filter_by_state(transactions, status_type)

    print(f'Операции отфильтрованы по статусу "{status_type}"\n')


    # Сортировка по дате
    sorting_by_date = input("Отсортировать операции по дате? Да/Нет\n").lower()

    while sorting_by_date not in ["да", "нет"]:
        sorting_by_date = input('Пожалуйста, введите "да" или "нет"\n').lower()

    if sorting_by_date == "да":
        descending = input("Отсортировать по возрастанию или по убыванию?\n").lower()

        while descending not in ["по возрастанию", "по убыванию"]:
            descending = input('Пожалуйста, введите "по возрастанию" или "по убыванию"\n').lower()

        if descending == "по убыванию":
            sorted_by_date = sort_by_date(transactions_by_status)
        else:
            sorted_by_date = sort_by_date(transactions_by_status, False)

    else:
        sorted_by_date = transactions_by_status



    # Сортировка по валюте
    only_rub = input("Выводить только рублевые транзакции? Да/Нет\n").lower()

    while only_rub not in ["да", "нет"]:
        only_rub = input('Пожалуйста, введите "да" или "нет"\n').lower()

    if only_rub == "да":
        filtered_by_currency = list(filter_by_currency(sorted_by_date, "RUB"))
    else:
        filtered_by_currency = sorted_by_date



    # Поиск по транзакциям
    search_in_transactions = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()

    while search_in_transactions not in ["да", "нет"]:
        search_in_transactions = input('Пожалуйста, введите "да" или "нет"\n').lower()

    if search_in_transactions == "да":
        search_word = input("Введите слово для поиска:\n")
        sorted_transactions = search_transactions(filtered_by_currency, search_word)
    else:
        sorted_transactions = filtered_by_currency



    print("Распечатываю итоговый список транзакций...")



    if len(sorted_transactions) > 0:
        print(f"Всего банковских операций в выборке: {len(sorted_transactions)}")

        for transaction in sorted_transactions:

            date = get_date(transaction["date"])
            description = transaction["description"]
            to_ = mask_account_card(transaction["to"])
            summa, currency = transaction["amount"], transaction["currency_name"]

            if transaction.get("from") and str(transaction["from"]) != "nan":
                from_to = f"{mask_account_card(transaction.get("from"))} -> {to_}"
            else:
                from_to = f"{mask_account_card(to_)}"

            print(f"\n{date} {description}\n{from_to}\nСумма: {summa} {currency}")


    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации\n")
