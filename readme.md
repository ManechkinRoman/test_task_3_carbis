# Программа для получения координат объекта по его адресу

Данная программа не имеет встроенных настроек и использует официальную библиотеку dadata для получения данных с сервиса DaData.

## Зависимости:

-   Python 3.7+
-   [DaData](https://github.com/hflabs/dadata-py)

## Установка

Для установки программы необходимо скачать её из текущего репозитория, установить зависимости из файла requirements.txt,
а также установить ваш API ключ для сервиса DaData в переменную окружения с именем MY_DADATA_API.

Для установки зависимостей программы нужно выполнить следующую команду в директории программы:

```
pip install -r requirements.txt
```

Для установки переменной окружения в ОС Linux воспользуйтесь следующей командой:

```
MY_DADATA_API="<ваш API ключ>"
```

Для установки переменной окружения в ОС Windows воспользуйтесь google.

## Использование

Для запуска программы используйте следующую команду:
```
python3 main.py
```

### Программа имеет следующий функционал:

Получение справки о программе:
```
help
```

Получение координат объекта по адресу:
```
get coords <адрес объекта>
```
> Важно! После этой команды пользователю будет предложено выбрать уточненный адрес объекта с помощью ввода цифры от 0 до 6.

Выход из программы:
```
exit
```


