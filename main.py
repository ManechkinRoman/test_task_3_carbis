# Импортируем необходимые модули
import sys  # модуль для работы со стандартными потоками ввода вывода
from dadata import Dadata  # модуль для работы с Dadata API
import os  # модуль для получения переменных окружения

HELP_MESSAGE = f"Help для программы получения точных координат объекта по адресу.\n" \
               f"1.\tЧтобы получить координаты объекта введите: 'get cords <адрес объекта>'.\n" \
               f"\tДалее вам будет предложено выбрать уточненный адрес объекта, введите цифру в указанном диапазоне.\n" \
               f"\tПосле этого вы получите точные координаты адреса объекта.\n" \
               f"2.\tДля получения помощи введите команду help.\n" \
               f"3.\tДля выхода из программы введите команду exit.\n" \
               f"4.\tДля получения справки пишите на электронный адрес: romanmanechkin@yandex.ru\n"


def get_correct_addresses(addr, count=7):
    """Функция возвращает список корректных адресов"""
    # производим запрос
    query_result = dadata.suggest(name="address", query=addr, count=count)
    # получаем нужные данные
    result = []
    for line in query_result:
        result.append(line["unrestricted_value"])
    # возвращаем список уточненных адресов
    return result


def get_cords(address):
    """Функция возвращает координаты для уточненного адреса."""
    # производим запрос
    correct_address_obj = dadata.suggest(name="address", query=address, count=1)
    # получаем нужные данные
    lat = correct_address_obj[0]["data"]["geo_lat"]
    lon = correct_address_obj[0]["data"]["geo_lon"]
    # возвращаем координаты объекта
    return lat, lon


def main():
    global dadata   # для удобства сделаем объект глобальным
    result = None   # переменная для хранения результатов уточняющего запроса

    std_input = sys.stdin  # модуль потока входных данных
    std_out = sys.stdout  # модуль потока выходных данных

    # Выведем приветственное сообщение
    std_out.write(f"Вы запустили программу для получения точных координат объекта по адресу.\n"
                  f"Для получения справки напишите help.\n"
                  f"Для выхода из программы напишите exit\n")

    # Получим API из переменных окружения и создадим объект dadata
    try:
        token = os.getenv("MY_DADATA_API")
        dadata = Dadata(token)
        std_out.write("Получен API_token для Dadata.\n")
    except Exception as error:
        # В случае ошибки выходим из программы
        std_out.write(f"Не получилось получить токен для Dadata. \n Ошибка: \n {error}\n")
        exit(0)

    # Цикл чтения входного потока данных (работает бесконечно!)
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
            address = line.strip()[10:]   # получим адрес из сообщения пользователя
            result = get_correct_addresses(address) # получим результат запроса к dadata по адресу пользователя
            std_out.write("Выберите уточненный вариант адреса:\n")
            # Вывод уточненных адресов
            for indx, adr in enumerate(result):
                std_out.write(f"[{indx}]\t {adr}\n")
            std_out.write(f"Введите цифру от 0 до {len(result)}:\n")

        # Если пользователь ввел цифру и до этого был произведен запрос с уточнением адресов, то получим координаты
        # уточненного адреса
        elif line.strip().isdigit() and result:
            # проверка на корректность введенной цифры
            if not int(line.strip()) in range(len(result)):
                print("Вы выбрали неверный адрес. Введите корректную цифру.")
                continue

            std_out.write(f"Вывод точных координат запроса № {line.strip()}\n")
            address = result[int(line.strip())]     # достаем уточненный адрес объекта из запроса
            # получаем координаты выбранного адреса
            lat, lon = get_cords(address)
            # выводим результат
            std_out.write(f"Координаты выбранного объекта: {lat}, {lon}\n")
            result = None

        # сообщение о некорректном вводе пользователя
        else:
            std_out.write(f"Введено некорректное сообщение.\n")


if __name__ == "__main__":
    main()
