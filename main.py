# Импортируем необходимые модули
import sys  # модуль для работы со стандартными потоками ввода вывода
from dadata import Dadata  # модуль для работы с Dadata API
import os  # модуль для получения переменных окружения

# УБРАТЬ КЛЮЧЬ ПЕРЕД ЗАЛИВКОЙ НА GIT!
HELP_MESSAGE = f"Help для программы получения точных координат объекта по адресу.\n" \
               f"1.\tЧтобы получить координаты объекта введите: 'get cords <адрес объекта>'.\n" \
               f"\tДалее вам будет предложено выбрать уточненный адрес объекта, введите цифру в указанном диапазоне.\n" \
               f"\tПосле этого вы получите точные координаты адреса объекта.\n" \
               f"2.\tДля получения помощи введите команду help.\n" \
               f"3.\tДля выхода из программы введите команду exit.\n" \
               f"4.\tДля получения справки пишите на электронный адрес: romanmanechkin@yandex.ru\n"


def get_correct_addresses(addr):
    """Функция возвращает список корректных адресов"""
    global dadata
    query_result = dadata.suggest(name="address", query="Новосибирск Новогодняя 12")

    result = []
    for line in query_result:
        result.append(line["unrestricted_value"])
    return result


def main():
    global dadata
    result = None
    dadata = None

    std_input = sys.stdin  # модуль потока входных данных
    std_out = sys.stdout  # модуль потока выходных данных

    # Выведем приветственное сообщение
    std_out.write(f"Вы запустили программу для получения точных координат объекта по адресу.\n"
                  f"Для Получения справки напишите help.\n"
                  f"Для выхода из программы напишите exit\n")

    # Получим API из переменных окружения
    try:
        token = os.getenv("MY_DADATA_API")
        dadata = Dadata(token)
        std_out.write("Получен API_token для Dadata.\n")
    except Exception as error:
        std_out.write(f"Не получилось получить токен для Dadata. \n Ошибка: \n {error}\n")

    # цикл чтения входного потока данных
    for line in std_input:
        # Завершение работы программы если получено сообщение 'exit'
        if "exit" == line.strip():
            std_out.write("Производим выход из программы.\n")
            exit(0)
        # получение справки
        elif "help" == line.strip():
            std_out.write(HELP_MESSAGE)
        # получение координат
        elif "get cords" in line.strip():
            address = line.strip()[10:]
            result = get_correct_addresses(address)
            std_out.write("Выберите уточненный вариант адреса:\n")
            for indx, adr in enumerate(result):
                std_out.write(f"[{indx}]\t {adr}\n")
            std_out.write(f"Введите цифру от 0 до {len(result)}:\n")

        elif line.strip().isdigit() and result:
            std_out.write(f"Вывод точных координат запроса № {line.strip()}\n")
        else:
            std_out.write(f"Введено некорректное сообщение.\n")


if __name__ == "__main__":
    main()
