# Проект "BankWidget"

## Описание и цель проекта:

Проект представляет собой серверную часть виджета банковских операций. Виджет имеет возможность

- отображать операции клиента и их описание;
- показывать несколько последних успешных банковских операций;
- регистрировать детали выполнения операций и информацию об ошибках;
- считывать данные с JSON-, CSV- и XLSX_файлов,
- сортировать операции по статусу, дате, валюте, ключевым словам.

## Установка:

1. Клонируйте [репозиторий](https://github.com/nex-kex/BankWidget):

`git clone git@github.com:nex-kex/BankWidget.git`

2. Установите зависимости:

`pip install -r requirements.txt`

## Использование:

1. Запустите программу в модуле `main.py` в корневой директории `src/`.

2. Программа будет задавать вопросы о сортировке, ответ нужно печатать текстом (регистр не важен).

## Тестирование:

Для запуска тестов выполните команду:

`pytest`

Для получения информации о покрытии тестами выполните команду:

- При активном виртуальном окружении: `pytest --cov`

- Через Poetry: `poetry run pytest --cov`

Информацию о покрытии тестами можно посмотреть в HTML отчёте. Для этого необходимо открыть в браузере файл `index.html`
из папки `htmlcov\`.

## Примеры работ с функциями:

1. Модуль `masks`:

```
print(get_mask_card_number(7000792289606361))
>>> 7000 79** **** 6361

print(get_mask_account(73654108430135874305))
>>> **4305
```

2. Модуль `widget`:

```
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("MasterCard 7158300734726758"))
>>> Visa Platinum 8990 92** **** 5229
>>> Счет **4305
>>> MasterCard 7158 30** **** 6758

print(get_date("2024-03-11T02:26:18.671407"))
>>> 11.03.2024
```

3. Модуль `processing`:

```
print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

4. Модуль `generators`:

```
transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD"
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "amount": "79114.93",
            "currency_name": "USD",
            "currency_code": "USD"
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "amount": "43318.34",
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "amount": "56883.54",
            "currency_name": "USD",
            "currency_code": "USD"
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "amount": "67314.70",
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

print(list(filter_by_currency(transactions, "RUB")))
>>> 
[
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "amount": "43318.34", 
        "currency_name": "руб.", 
        "currency_code": "RUB",
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "amount": "67314.70", 
        "currency_name": "руб.", 
        "currency_code": "RUB",
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

print(list(transaction_descriptions(transactions)))
>>> 
[
    "Перевод организации",
    "Перевод со счета на счет",
    "Перевод со счета на счет",
    "Перевод с карты на карту",
    "Перевод организации",
]

print(list(card_number_generator(1, 5)))
>>> 
[
    "0000 0000 0000 0001",
    "0000 0000 0000 0002",
    "0000 0000 0000 0003",
    "0000 0000 0000 0004",
    "0000 0000 0000 0005"
]
```

5. Модуль `decorators`:

```
@log()
def my_function(x, y):
    return x + y
my_function(1, 2)
>>> 
my_function executed with no errors. Input args: (1, 2), kwargs: {}. Execution time: 0.00000143 seconds.

@log()
def my_function(x, y):
    return x / y
my_function(1, 0)
>>>
my_function executed with an error: division by zero. Input args: (1, 0), kwargs: {}. Execution time: 0.00000787 seconds.
```

6. Модуль `read_from_table`:

```
print(read_from_csv("../data/transactions.csv")
>>>
[{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 
        'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 
        'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
       {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740',
        'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
        'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'} 
... ]

print(read_from_xlsx("../data/transactions_excel.xlsx")
>>>
[{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 
        'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 
        'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
       {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740',
        'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
        'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'} 
... ]
```

7. Модуль `search`:

```
print(search_transactions(transactions, "организации"))
>>> 
[{
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "amount": "9824.07",
    "currency_name": "USD",
    "currency_code": "USD",
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
},
{
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "amount": "67314.70",
    "currency_name": "руб.",
    "currency_code": "RUB",
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
}]
        
print(filter_by_category(transactions, ["Перевод организации", "Перевод с карты на карту"]))
>>>
{"Перевод организации": 2, "Перевод с карты на карту": 1}
```