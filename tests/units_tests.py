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


def test_mask_number():

    test1 = "Счет 41421565395219882431"
    test2 = "MasterCard 3152479541115065"
    test3 = "Visa Gold 9447344650495960"
    test4 = "Visa Platinum 2256483756542539"
    result1 = mask_number(test1)
    result2 = mask_number(test2)
    result3 = mask_number(test3)
    result4 = mask_number(test4)
    expectation1 = "Счет **2431"
    expectation2 = "MasterCard 3152 31** **** 5065"
    expectation3 = "Visa Gold 9447 94** **** 5960"
    expectation4 = "Visa Platinum 2256 22** **** 2539"

    assert result1 == expectation1, "Вывод совпадает с ожидаемым"
    assert result2 == expectation2, "Вывод совпадает с ожидаемым"
    assert result3 == expectation3, "Вывод совпадает с ожидаемым"
    assert result4 == expectation4, "Вывод совпадает с ожидаемым"


