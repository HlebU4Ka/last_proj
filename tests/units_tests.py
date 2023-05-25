import os, datetime

from src.units import mask_number, read_json_file, json, data_json

date = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
  {
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2019-08-19T04:27:37.904916",
    "operationAmount": {
      "amount": "56883.54",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 6831982476737658",
    "to": "Visa Platinum 8990922113665229"
  },
  {
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {
      "amount": "43318.34",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
  },
  {
    "id": 214024827,
    "state": "EXECUTED",
    "date": "2018-12-20T16:43:26.929246",
    "operationAmount": {
      "amount": "70946.18",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 10848359769870775355",
    "to": "Счет 21969751544412966366"
  },
  {
    "id": 522357576,
    "state": "EXECUTED",
    "date": "2019-07-12T20:41:47.882230",
    "operationAmount": {
      "amount": "51463.70",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 48894435694657014368",
    "to": "Счет 38976430693692818358"
  }]

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

    print("Тестирование функции read_json_file() успешно завершено.")


# Вызов функции для тестирования
test_read_json_file()


# def test_mask_number():
#
#     test1 = "Счет 41421565395219882431"
#     test2 = "MasterCard 3152479541115065"
#     test3 = "Visa Gold 9447344650495960"
#     test4 = "Visa Platinum 2256483756542539"
#     result1 = mask_number(test1)
#     result2 = mask_number(test2)
#     result3 = mask_number(test3)
#     result4 = mask_number(test4)
#     expectation1 = "Счет **2431"
#     expectation2 = "MasterCard 3152 31** **** 5065"
#     expectation3 = "Visa Gold 9447 94** **** 5960"
#     expectation4 = "Visa Platinum 2256 22** **** 2539"
#
#     assert result1 == expectation1, "Вывод совпадает с ожидаемым"
#     assert result2 == expectation2, "Вывод совпадает с ожидаемым"
#     assert result3 == expectation3, "Вывод совпадает с ожидаемым"
#     assert result4 == expectation4, "Вывод совпадает с ожидаемым"

def test_mask_number():
    test_cases = [
        ("Счет 41421565395219882431", "Счет **2431"),
        ("MasterCard 3152479541115065", "MasterCard 3152 31** **** 5065"),
        ("Visa Gold 9447344650495960", "Visa Gold 9447 94** **** 5960"),
        ("Visa Platinum 2256483756542539", "Visa Platinum 2256 22** **** 2539")
    ]

    for test_input, expected_output in test_cases:
        result = mask_number(test_input)
        assert result == expected_output, "Вывод совпадает с ожидаемым"

test_mask_number()

def test_keys():
    for item in date:
        assert "id" in item
        assert "state" in item
        assert "date" in item
        assert "operationAmount" in item
        assert "description" in item
        assert "from" in item or "to" in item

def test_required_fields():
    for item in date:
        if item["description"] == "Перевод организации":
            assert "from" in item, f"'from' файл отсутсвует: {item}"
            assert "to" in item, f"'to' field is missing: {item}"
        elif item["description"] == "Перевод с карты на карту":
            assert "from" in item, f"'from' файл отсутсвует: {item}"
            assert "to" in item, f"'to' файл отсутсвует: {item}"
        elif item["description"] == "Перевод со счета на счет":
            assert "from" in item, f"'from' файл отсутсвует: {item}"
            assert "to" in item, f"'to' файл отсутсвует: {item}"
        elif item["description"] == "Открытие вклада":
            assert "to" in item, f"'to' файл отсутсвует: {item}"

def test_date_format():


    for item in date:
        date_str = item["date"]
        try_date = datetime.datetime.fromisoformat(date_str).strftime('%d.%m.%Y')
        try:
            formatted_date = datetime.datetime.fromisoformat(date_str).strftime('%d.%m.%Y')
        except ValueError:
            assert False, f"Недопустимый формат: {date_str}"
        assert formatted_date == try_date, f"Формат даты не соответствует ожидаемому формату: {try_date}"




