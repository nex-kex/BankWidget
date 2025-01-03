# Проект "BankWidget"

##  Описание и цель проекта:

Проект представляет собой серверную часть виджета банковских операций. Виджет имеет возможность 
- отображать операции клиента;
- показывать несколько последних успешных банковских операций; 
- сортировать операции по дате.

## Установка:

1. Клонируйте [репозиторий](https://github.com/nex-kex/BankWidget):

`git clone git@github.com:nex-kex/BankWidget.git`

2. Установите зависимости:

`pip install -r requirements.txt`

## Использование:

*в процессе*

## Тестирование:

Для запуска тестов выполните команду:

- При активном виртуальном окружении: `pytest --cov`

- Через Poetry: `poetry run pytest --cov`

Информацию о покрытии тестами можно посмотреть в HTML отчёте. Для этого необходимо открыть в браузеер файл `index.html` из папки `htmlcov\`.

## Примеры работ с функциями:

```
print(get_mask_card_number(7000792289606361))
>>> 7000 79** **** 6361

print(get_mask_account(73654108430135874305))
>>> **4305

print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("MasterCard 7158300734726758"))
>>> Visa Platinum 8990 92** **** 5229
>>> Счет **4305
>>> MasterCard 7158 30** **** 6758

print(get_date("2024-03-11T02:26:18.671407"))
>>> 11.03.2024

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
