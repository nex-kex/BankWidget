from masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Функция для обработки информации о картах и счетах"""
    if data[:4] == "Счет":
        return f"Счет {get_mask_account(data[-20:])}"
    else:
        return f"{data[:-17]} {get_mask_card_number(data[-16:])}"