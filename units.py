import json
data_json = ".../final_project/operations.json"


def read_json_file(file_path :str):
    """
        Читает данные из файла JSON.

        Аргументы:
        file_path (str): Путь к файлу JSON.

        Возвращает:
        dict: Содержимое файла JSON в виде словаря.
        """


    with open(data_json, 'r') as file:
        data = json.load(file)
        return data


print(read_json_file(data_json))


