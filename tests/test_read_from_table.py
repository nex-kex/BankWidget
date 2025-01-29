from unittest.mock import patch, mock_open
import pandas as pd
from src.read_from_table import read_from_csv, read_from_xlsx


@patch(
    "builtins.open",
    mock_open(
        read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n1;2;3;4;5;6;7;8;9\n11;22;33;44;55;66;77;88;99\n"
    ),
)
def test_read_from_csv(csv_transactions):
    assert read_from_csv("") == csv_transactions


@patch("builtins.open", mock_open(read_data=""))
def test_read_from_csv_empty():
    assert read_from_csv("") == []


@patch("pandas.read_excel")
def test_read_from_xlsx(mock_read_excel, csv_transactions):
    mock_read_excel.return_value = pd.DataFrame({
            "id": ["1", "11"],
            "state": ["2", "22"],
            "date": ["3", "33"],
            "amount": ["4", "44"],
            "currency_name": ["5", "55"],
            "currency_code": ["6", "66"],
            "from": ["7", "77"],
            "to": ["8", "88"],
            "description": ["9", "99"],
        })
    assert read_from_xlsx("") == csv_transactions


@patch("pandas.read_excel")
def test_read_from_xlsx_empty(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame({})
    assert read_from_xlsx("") == []
