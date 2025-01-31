from src.read_from_table import read_from_csv, read_from_xlsx
from src.utils import get_transactions_info
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.search import search_transactions
from src.widget import get_date, mask_account_card


def get_transactions() -> list[dict]:
    """Спрашивает у пользователя, в каком формате получить данные
    и возвращает транзакции из соответствующего файла."""

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

    return transactions


def get_state_sorted_transactions(transactions: list[dict]) -> list[dict]:
    """Спрашивает у пользователя, по какому статусу необходимо выполнить фильтрацию
    и возвращает список транзакций с соответствующим статусом."""

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

    return transactions_by_status


def get_date_sorted_transactions(transactions_by_status: list[dict]) -> list[dict]:
    """Спрашивает у пользователя, нужно ли сортировать по дате. Если да - то в каком порядке
    (по убыванию или возрастанию), возвращает список отсортированных по дате транзакций."""

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

    return sorted_by_date


def get_currency_sorted_transactions(sorted_by_date: list[dict]) -> list[dict]:
    """Спрашивает у пользователя, нужно ли выводить только транзакции в рублях.
    Если да - возвращает список транзакций в рублях, если нет - всех транзакций."""

    only_rub = input("Выводить только рублевые транзакции? Да/Нет\n").lower()

    while only_rub not in ["да", "нет"]:
        only_rub = input('Пожалуйста, введите "да" или "нет"\n').lower()

    if only_rub == "да":
        filtered_by_currency = list(filter_by_currency(sorted_by_date, "RUB"))
    else:
        filtered_by_currency = sorted_by_date

    return filtered_by_currency


def get_search_sorted_transactions(filtered_by_currency: list[dict]) -> list[dict]:
    """Спрашивает у пользователя, нужно ли искать в транзакциях определённое слово.
    Если да - спрашивает слово и возвращает список тех транзакций, у которых оно встречается в описании."""

    search_in_transactions = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()

    while search_in_transactions not in ["да", "нет"]:
        search_in_transactions = input('Пожалуйста, введите "да" или "нет"\n').lower()

    if search_in_transactions == "да":
        search_word = input("Введите слово для поиска:\n")
        sorted_transactions = search_transactions(filtered_by_currency, search_word)
    else:
        sorted_transactions = filtered_by_currency

    return sorted_transactions


def print_result(sorted_transactions: list[dict]) -> None:
    """Выводит найденные транзакции или сообщение о том, что не было найдено подходящих."""

    print("\nРаспечатываю итоговый список транзакций...\n")

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


if __name__ == "__main__":
    transactions = get_transactions()
    transactions_by_status = get_state_sorted_transactions(transactions)
    sorted_by_date = get_date_sorted_transactions(transactions_by_status)
    filtered_by_currency = get_currency_sorted_transactions(sorted_by_date)
    sorted_transactions = get_search_sorted_transactions(filtered_by_currency)
    print_result(sorted_transactions)
