from functools import wraps
from time import time
from typing import Any, Callable


def log(filename: str = "") -> Callable:
    """Декоратор, который логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
    Декоратор принимает необязательный аргумент filename, который определяет, куда будут записываться логи"""

    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> None:

            # Время начала выполнения
            start_time = time()

            # Проверка на наличие ошибок
            try:
                func(*args, **kwargs)
                new_log = f"{func.__name__} executed with no errors. "
            except Exception as e:
                new_log = f"{func.__name__} executed with an error: {e}. "

            # Время окончания выполнения
            end_time = time()
            new_log = (
                new_log
                + f"Input args: {args}, kwargs: {kwargs}. Execution time: {end_time - start_time:.8f} seconds.\n"
            )

            # Запись в файл или вывод в консоль
            if filename != "":
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(new_log)
            else:
                print(new_log)

        return wrapper

    return my_decorator
