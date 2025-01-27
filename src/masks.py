from typing import Union
import logging


log_path = "./logs/masks.log"

# Устраняет ошибку отсутствия файла при импорте модуля
if __name__ == "__main__":
    log_path = "." + log_path


logger = logging.getLogger("masks")
file_handler = logging.FileHandler(log_path, "w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    try:
        # Номер карты в строковом формате
        s: str = str(card_number)

        if len(s) != 16:
            logger.warning(f"Masked a card with wrong length: {len(s)} when 16 is required.")
        else:
            logger.info("Successfully masked card number.")

    except Exception as ex:
        logger.error(f"Exception occurred: {ex}")

    return f"{s[0:4]} {s[4:6]}** **** {s[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску"""

    try:
        # Номер счёта в строковом формате
        s: str = str(account_number)

        if len(s) != 20:
            logger.warning(f"Masked an account with wrong length: {len(s)} when 20 is required.")
        else:
            logger.info("Successfully masked account number.")

    except Exception as ex:
        logger.error(f"Exception occurred: {ex}")

    return f"**{s[-4:]}"
