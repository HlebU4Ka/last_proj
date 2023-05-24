import json
data_json = "operations.json"


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



def mask_number(sub):
    """
    Замаскировать номер карты.

    Разбивает входную строку на слова, извлекает последнее слово (номер карты),
    и замаскированный номер карты возвращается в заданном формате.

    Параметры:
    - sub (str): Входная строка, содержащая номер карты.

    Возвращает:
    str: Замаскированный номер карты.

    """
    my_list = sub.split(" ") # Массив из слов
    card_number = my_list[-1] # Последние цифры
    if (my_list[0] != "Счет"):
        # card_number = card_number[:6] + "*" * 6 + card_number[12:]
        card_number = card_number[:4] + " " + card_number[:2] + "** ****" + " " + card_number[-4:]

    else:
        card_number = "**" + card_number[-4:]
    my_list[-1] = card_number
    return " ".join(my_list)


