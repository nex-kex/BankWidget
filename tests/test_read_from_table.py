from unittest.mock import patch, mock_open
import csv
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