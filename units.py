import json


file_path = "operations.json"


def read_json_file(file_path):

    """
        Читает данные из файла JSON.

        Аргументы:
        file_path (str): Путь к файлу JSON.

        Возвращает:
        dict: Содержимое файла JSON в виде словаря.
    """


    with open(file_path, 'r', encoding='utf-8') as file:

        data = json.load(file)

    return data

# print(read_json_file(data_json)["id"])


def mask_card_number(card_number, account_number):

    """
    Функция маскирует номер карты
    card_number - передается по номеру содержимое Json файла после прочтения
    (предворительно номер карты)
    """
    masked_kard_number = "{} XX** **** {}".format(card_number[:6], card_number[-4:])

    """
    Функция маскирует номер счета
    account_number - передается по номеру содержимое Json файла после прочтения
    (предворительно номер счета)
    """

    masked_number = "**{}".format(account_number[-4:])
    return masked_number, masked_kard_number


# def range_number(file_path):
#     for key in range(1, 5):
#         value = read_json_file(file_path)[key]
#
#     return value
#
# print(range_number)