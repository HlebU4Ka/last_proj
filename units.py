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


