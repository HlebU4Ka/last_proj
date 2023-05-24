from src.units import mask_number, read_json_file, json, data_json
import os


def test_read_json_file():
    """
    Функция для тестирования функции read_json_file().
    """

    # Тестовый файл JSON
    test_file = 'test.json'

    # Создание тестовых данных
    data = {
        'name': 'John Doe',
        'age': 25,
        'city': 'New York'
    }
    with open(test_file, 'w') as file:
        json.dump(data, file)

    # Вызов функции read_json_file()
    result = read_json_file(test_file)

    # Проверка результата
    assert isinstance(result, dict), "Результат должен быть словарем"
    assert result == data, "Содержимое файла JSON не совпадает с ожидаемым"

    # Удаление тестового файла
    os.remove(test_file)

    print("Тестирование функции read_json_file() успешно завершено.")


# Вызов функции для тестирования
test_read_json_file()



