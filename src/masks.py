def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    # Номер карты в строковом формате
    s: str = str(card_number)

    return f"{s[0:4]} {s[4:6]}** **** {s[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску"""

    # Номер счёта в строковом формате
    s: str = str(account_number)

    return f"**{s[-4:]}"
